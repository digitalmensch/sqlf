#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `sqlf` package."""

# import pytest
import sqlf


###############################################################################
# Data Serialisation UDFs
###############################################################################


def test_cbor_map():
    @sqlf.single_row
    @sqlf.sqlf
    def test():
        ''' select cbor_map() as m; '''
    assert {'m': b'\xa0'} == test()


def test_cbor_insert():
    @sqlf.single_row
    @sqlf.sqlf
    def test():
        ''' select cbor_insert(cbor_map(), 'n', 3.14) as m; '''
    assert {'m': b'\xa1an\xfb@\t\x1e\xb8Q\xeb\x85\x1f'} == test()


def test_cbor_has():
    @sqlf.single_row
    @sqlf.sqlf
    def test():
        ''' select cbor_has(cbor_insert(cbor_map(), 'n', 3.14), 'n') as m; '''
    assert {'m': 1} == test()
