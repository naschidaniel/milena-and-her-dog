# -*- coding: utf-8 -*-

import os
import shlex
import shutil
import sys
import datetime

from invoke import task
from invoke.main import program
from invoke.util import cd
from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

SETTINGS_FILE_BASE = 'pelicanconf.py'
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    'settings_base': SETTINGS_FILE_BASE,
    'settings_publish': 'publishconf.py',
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    'deploy_path': SETTINGS['OUTPUT_PATH'],
    # Host and port for `serve`
    'host': 'localhost',
    'port': 8000,
}

@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG['deploy_path']):
        shutil.rmtree(CONFIG['deploy_path'])
        os.makedirs(CONFIG['deploy_path'])

@task
def build(c):
    """Build local version of site"""
    set_environment_variables(c)
    pelican_run('-s {settings_base}'.format(**CONFIG))

@task
def rebuild(c):
    """`build` with the delete switch"""
    pelican_run('-d -s {settings_base}'.format(**CONFIG))

@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    pelican_run('-r -s {settings_base}'.format(**CONFIG))

@task
def serve(c):
    """Serve site at http://$HOST:$PORT/ (default is localhost:8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG['deploy_path'],
        (CONFIG['host'], CONFIG['port']),
        ComplexHTTPRequestHandler)

    sys.stderr.write('Serving at {host}:{port} ...\n'.format(**CONFIG))
    server.serve_forever()

@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)


@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server
    build(c)
    server = Server()
    # Watch the base settings file
    server.watch(CONFIG['settings_base'], lambda: build(c))
    # Watch content source files
    content_file_extensions = ['.md', '.rst']
    for extension in content_file_extensions:
        content_blob = '{0}/**/*{1}'.format(SETTINGS['PATH'], extension)
        server.watch(content_blob, lambda: build(c))
    # Watch the theme's templates and static assets
    theme_path = SETTINGS['THEME']
    server.watch('{}/templates/*.html'.format(theme_path), lambda: build(c))
    static_file_extensions = ['.css', '.js']
    for extension in static_file_extensions:
        static_file = '{0}/static/**/*{1}'.format(theme_path, extension)
        server.watch(static_file, lambda: build(c))
    # Serve output path on configured host and port
    server.serve(host=CONFIG['host'], port=CONFIG['port'], root=CONFIG['deploy_path'])


@task
def kill(c):
    """Terminate all processes on port 8000"""
    c.run("kill -9 $(lsof -i TCP:8000 | grep LISTEN | awk '{print $2}')")

@task
def npm_install(c):
    """Install node Components"""
    c.run("npm install")

@task
def npm_dev(c):
    """Generate js and css Components for development"""
    c.run("npm run-script dev")

@task
def npm_build(c):
    """Build js and css Components for production"""
    c.run("npm run-script build")

@task
def development(c):
    """Generate css and js files and start the livereload server"""
    clean(c)
    npm_dev(c)
    livereload(c)

@task
def preview(c):
    """Build a Blog preview for localhost"""
    clean(c)
    npm_build(c)
    build(c)

@task
def publish(c):
    """Build for gh-pages"""
    clean(c)
    set_environment_variables(c)
    pelican_run('-s {settings_publish}'.format(**CONFIG))


@task
def set_environment_variables(c):
    """A function to write local environment variables"""
    lastcommit = c.run("git rev-parse --short HEAD")
    lastcommit = lastcommit.stdout.strip()
    print(f"The last commit number is {lastcommit}.")

    env_variables = {"LASTCOMMIT": lastcommit}
    try:
        with open(".env", "w") as f:
            for key, value in env_variables.items():
                f.write(f"{key}={value}\n")
            f.close()
        print("The environment file was written.")

    except:
        print("The environment variable cannot be written.")


def pelican_run(cmd):
    cmd += ' ' + program.core.remainder  # allows to pass-through args to pelican
    pelican_main(shlex.split(cmd))