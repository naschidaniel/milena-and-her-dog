#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Daniel Naschberger'
SITENAME = 'milena-and-her-dog.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

GITHUB_URL = 'https://github.com/naschidaniel/milena-and-her-dog'


# Template
THEME = 'themes/milena'
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'main.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social links
SOCIALLINKS = {'Instagram': '#instagram',
               'Facebook': '#facebook',
               'Pinterrest': '#pinterrest'
              }

DEFAULT_PAGINATION = 5

# Date Formats
DATE_FORMATS = {
    'de': '%d.%m.%Y',
    }

# path-specific metadata
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    }

# Static files
STATIC_PATHS = [
    'images',
    'static/robots.txt',
    ]

# URL Settings
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '/{slug}'
PAGE_SAVE_AS = '{slug}/index.html'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True