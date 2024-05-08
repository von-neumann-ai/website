# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Von Neumann AI'
copyright = '2024, Sasank Chilamkurthy'
author = 'Sasank Chilamkurthy'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Von Neumann AI"
html_favicon = "_static/favicon.ico"
html_theme = 'furo'
html_static_path = ['_static']
html_theme_options = {
    "light_logo": "logo-light.png",
    "dark_logo": "logo-dark.png",
    "light_css_variables": {
        "color-brand-primary": "#2D1A6D",
        "color-brand-content": "#2D1A6D",
        "color-content-foreground": "#2D1A6D"
    },
    "dark_css_variables": {
        "color-brand-primary": "white",
        "color-brand-content": "white",
        "color-content-foreground": "white",
        "color-background-primary": "#0A031D",
        "color-background-secondary": "#0A031D",
    },
    "sidebar_hide_name": True,
}

extensions = [
    'myst_parser', 
    'sphinxcontrib.video']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
