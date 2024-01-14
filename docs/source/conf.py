# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Triform'
copyright = '2024, Movsai'
author = 'Iggy@Movsai'

release = '0.1'
version = '0.1.0'

# -- General configuration

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',  # Markdown support
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output

# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Source file parsers
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

html_sidebars = {
   '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']
}