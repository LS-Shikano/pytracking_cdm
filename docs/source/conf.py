import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "pytracking_cdm"
copyright = "2023, University of Konstanz - Center for Data and Methods"
author = "University of Konstanz - Center for Data and Methods"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.napoleon", "sphinx.ext.autodoc", "sphinx.ext.autosummary", 
"sphinx_autodoc_typehints"]

templates_path = ["_templates"]
exclude_patterns = []

autodoc_typehints = "description"  # document types in description
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries
set_type_checking_flag = True  # Enable 'expensive' imports for sphinx_autodoc_typehints
# autoapi_dirs = ['../../br_stimpy']
# autoapi_add_toctree_entry = False
# autoapi_template_dir = 'autoapi_templates'

# autosummary
autosummary_generate = True  # Turn on sphinx.ext.autosummary
autosummary_imported_members = True
add_module_names = False  # Remove namespaces from class/method signatures



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "piccolo_theme"  
html_static_path = ["_static"]
