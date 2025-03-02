# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'unittest2doc'
copyright = '2025, Fmajor'
author = 'Fmajor'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'sphinx.ext.napoleon',
  'sphinx.ext.autodoc',
  'sphinx.ext.autosummary',
  'sphinx_toolbox.collapse',
  'autodocsumm',
  'todo',
  'examples',
  'add_js', # fix the js bug in cloud theme (sphinx remove the jQuery and underscore library)
]

autosummary_generate = True  # Turn on sphinx.ext.autosummary

autodoc_default_options = {
  'autosummary': True,
  'members': True,
  'undoc-members': False,
  'show-inheritance': True,
  'private-members': False,
  'special-members': '__init__',
}

templates_path = ['_templates']
exclude_patterns = [
  "*.tests.rst",
  "*.tests_*.rst",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'cloud'
html_static_path = ['_static']

html_css_files = ["custom.css"]
html_js_files = [
  'jquery.js',
  'underscore.js',
]
html_theme_options = {
  "enable_search_shortcuts": True,
  #"body_max_width": 'none',
  # just for book_theme
  #"show_toc_level": 1,
  #"show_navbar_depth":10,
}
todo_include_todos = True

import os
import sys
# sys.path.insert(0, os.path.abspath('../../src/unittest2doc'))
import unittest2doc
sys.path.append(os.path.abspath("./_ext"))
repo_root = os.path.abspath('../../')
rst_epilog = f"""
.. |repo_root| replace:: {repo_root}
"""

autodoc_typehints = 'both'
autodoc_typehints_description_target = 'documented'
autodoc_default_flags = ['members']
html_sidebars = {
  '**': [
    'localtoc.html',
    'globaltoc.html',
    'sourcelink.html',
    'searchbox.html',
  ]
}