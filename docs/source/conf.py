# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Technologie webowe'
copyright = '2023, Leszek Imielski'
author = 'Leszek Imielski'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'pl'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme
html_theme = 'sphinx-rtd-theme'
html_static_path = ['_static']

master_doc = 'index'
# Dołącz konfigurację dla generowania plików PDF
#latex_documents = [
#     (master_doc, 'mybook.tex', 'Technologie', 'Leszek Imielski', 'article'),
# ]

