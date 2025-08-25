import os
import sys
from pathlib import Path
sys.path.append(str(Path('_ext').resolve()))

# sys.path.insert(0, os.path.abspath('_ext'))
# from volca_patch import VolcaPatchDirective
# from docutils.parsers.rst import directives
# def setup(app):
#     app.add_directive("volca-patch", VolcaPatchDirective)


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Coding Club'
copyright = '2023, Marcel Hrdina'
author = 'Marcel Hrdina'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        "sphinx.ext.todo",
        "sphinx_tags",
        "sphinx_rtd_theme",
        "sphinx_toolbox.collapse",
        "volca_patch"
        ]




templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


tags_create_tags = True

todo_include_todos = True

html_theme_options = {
        'collapse_navigation': False,
        'sticky_navigation': True,
        'navigation_depth': 4,
        'titles_only': False,
        }
