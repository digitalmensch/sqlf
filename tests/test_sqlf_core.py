#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `sqlf` package."""

import pytest
import sqlf
import types


###############################################################################
# sqlf.sql
###############################################################################


def test_sql_function():
    @sqlf.sql
    def test():
        ''' select 1 as one; '''
    assert test is not None
    assert isinstance(test, types.FunctionType)


def test_sql_function_yields_generator():
    @sqlf.sql
    def test():
        ''' select 1 as one; '''
    tmp = test()
    assert tmp is not None
    assert isinstance(tmp, types.GeneratorType)


@pytest.mark.parametrize("value", [(1, 3.14, '', b'', None, [], {})])
def test_sqlf_decorator_takes_function(value):
    with pytest.raises(TypeError):
        sqlf.sql(value)


###############################################################################
# sqlf.scalar_udf
###############################################################################


def test_scalar_udf_returns_function():
    def one():
        return 1
    two = sqlf.scalar_udf(one)
    assert one is two


def test_scalar_udf_registers_function():
    @sqlf.scalar_udf
    def one():
        return 1

    @sqlf.sql
    def _select_one():
        ''' select one() as one; '''
    assert [{'one': 1}] == list(_select_one())


###############################################################################
# sqlf.single_row
###############################################################################


@pytest.mark.parametrize("value", [1, 3.14, '', b'', None, [], {}])
def test_single_row_takes_generator_function(value):
    def it():
        yield {'one': 1}
    with pytest.raises(TypeError):
        sqlf.single_row(value)
    assert sqlf.single_row(it)() is not None


def test_single_row_returns_first_row():
    def it():
        yield {'one': 1}
        yield {'two': 2}
    val = sqlf.single_row(it)()
    assert 'one' in val
    assert val['one'] == 1


###############################################################################
# sqlf.as_type
###############################################################################


def test_as_type():
    @sqlf.as_type(lambda **kw: tuple(kw.keys()))
    @sqlf.sql
    def _test():
        ''' select 3.14 as pi, 11 as eleven; '''
    tmp = list(_test())[0]
    assert len(tmp) == 2
    assert 'pi' in tmp
    assert 'eleven' in tmp
