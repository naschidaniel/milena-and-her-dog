#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import sys
from dotenv import load_dotenv
load_dotenv()


AUTHOR = 'Daniel Naschberger'
SITENAME = 'milena-and-her-dog.com'
SITEURL = ''

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

GITHUB_URL = 'https://github.com/naschidaniel/milena-and-her-dog'


# Read Environment Variables
try:
    LASTCOMMIT = os.getenv("LASTCOMMIT")
except:
    print("Can not read .env file")
    sys.exit(1)

# Template
THEME = 'themes/milena'
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'main.css'

# META TAG INFORMATION
META_DESCRIPTION = 'Hi ich bin Milena! Auf meinem Blog erfährst du alles über mich und Frieda.'
META_KEYWORDS ='Milena, Frieda, Reisen, Stricken, Hund, Blog'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'))

# Social links
SOCIALLINKS = {'Instagram': 'https://www.instagram.com/milena_and_her_dog/',
               'Facebook': 'https://www.facebook.com/milenaandherdog/',
               'Pinterrest': 'https://www.pinterest.at/milenaandherdog/'
              }

DEFAULT_PAGINATION = 5

# Date Formats
DATE_FORMATS = {
    'de': '%d.%m.%Y',
    }

# path-specific metadata
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/CNAME': {'path': 'CNAME'},
    'static/.nojekyll': {'path': '.nojekyll'},
    }

# Static files
STATIC_PATHS = [
    'images',
    'static',
    ]

# URL Settings
PATH = 'content'
ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'

PAGE_PATHS = ['pages']
PAGE_URL = '/{slug}'
PAGE_SAVE_AS = '{slug}/index.html'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True