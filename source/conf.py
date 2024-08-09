project = 'Python Course'
copyright = '2024, David Landa'
author = 'David Landa'

extensions = [
    "myst_parser", # https://github.com/executablebooks/MyST-NB/issues/421
    # "myst_nb",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', ".venv"]

exclude_patterns += ['02/*.md']
exclude_patterns += ['03/*.md']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
