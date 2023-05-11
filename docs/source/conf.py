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

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]

templates_path = ["_templates"]
exclude_patterns = []


napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_use_rtype = True
napoleon_include_init_with_doc = True
add_module_names = False
autodoc_class_signature = "separated"
highlight_language = "python3"
autodoc_typehints = "signature"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "piccolo_theme"
html_static_path = ["_static"]
