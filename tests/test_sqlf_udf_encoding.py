#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `sqlf` package."""

# import pytest
import sqlf


###############################################################################
# Data Encoding UDFs
###############################################################################


def test_tohex():
    @sqlf.sql
    def _test(a):
        ''' select tohex(:a) as h; '''
    assert [{'h': '616263'}] == list(_test('abc'))
