# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme

project = 'SGL'
copyright = '2026, SGL All contributors'
author = 'SGL Team'
# release = 'SGL_20260101'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton',
    'myst_parser'
]


language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "sgl-org", # Username
    "github_repo": "sgl-docs", # Repo name
    "github_version": "main", # Version
    "conf_py_path": "/source/", # Path in the checkout to the docs root
}
html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = []
