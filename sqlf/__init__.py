# -*- coding: utf-8 -*-

"""Top-level package for SQL in F(unctions)."""

__author__ = """Digitalmensch"""
__email__ = "contact@digitalmensch.ch"
__version__ = "0.2.9"

from ._sqlf import sqlf
from ._sqlf import single_row
from ._sqlf import single_value
from ._sqlf import as_type

__all__ = ["as_type", "single_row", "single_value", "sqlf"]
