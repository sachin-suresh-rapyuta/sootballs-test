# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Testing...'
copyright = '2021, Graziella'
author = 'Graziella'

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

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

source_suffix = ['.rst', '.md']
master_doc = 'index'

exclude_patterns = ['_build']

pygments_style = 'sphinx'
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True, # Adding Rapyuta logo
    "collapse_navigation" : False
}

html_static_path = ['_static']
html_logo = "_static/rr-logo-vertical2022-1100px-transp.png"   # Adding Rapyuta logo

# -- Options for EPUB output
epub_show_urls = 'footnote'


rinoh_documents = [dict(doc='index',        # top-level file (index.rst)
                        target='pa-amr-specification-doc',
                        template='rinohtype.rtt',
                        logo='_static/rr-logo-vertical2022-1100px-transp.png')]   # output file (manual.pdf)


def setup(app):
    app.add_css_file('css/custom.css')