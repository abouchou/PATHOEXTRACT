# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'DREPAL-PATHOEXTRACT'
copyright = '2023, IPCI'
author = 'Stanislas Egomli ASSOHOUN (1-2) - Abouchou Paul Christian AKO (2)'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]


# Add contributors
contributors = [
    'Stanislas Egomli ASSOHOUN1-2',
    'Aristide Berenger AKO2',
    'Abouchou Paul Christian AKO2',
    'Catherine DAUGA3',
    'Jérôme Adou. KABLAN1',
    'Ronan JAMBOU2'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
