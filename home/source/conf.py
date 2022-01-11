# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx.application
import sphinx.errors
sphinx.application.ExtensionError = sphinx.errors.ExtensionError

# -- Project information -----------------------------------------------------

project = '3gee的哲学百科'
copyright = '2022, 3gee'
author = '3gee'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'nbsphinx',
    "sphinx.ext.graphviz",
    'sphinxcontrib.kroki',
    'sphinxcontrib.googleanalytics',
    "sphinx_comments",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

html_theme_options = {
    'repository_url' : 'https://github.com/threecifanggen/philosophia-wiki',
    "use_repository_button": True,
    "show_navbar_depth": 3
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

if sys.platform == 'win32':
    graphviz_dot_args = ['-Gfontname=Simsun', '-Efontname=Simsun', '-Nfontname=Simsun']

googleanalytics_id = "UA-56025474-6"

# 评论配置
comments_config = {
   "hypothesis": True,
   "utterances": {
      "repo": "threecifanggen/philosophia-wiki",
      "issue-term": "pathname",
      "crossorigin": "anonymous",
      "theme": "github-light"
   }
}


html_search_language = 'zh'
html_show_sourcelink = False
