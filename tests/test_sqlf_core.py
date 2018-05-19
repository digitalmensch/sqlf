#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `sqlf` package."""

import pytest
import sqlf
import types


###############################################################################
# sqlf.sqlf
###############################################################################


def test_sql_function():

    @sqlf.sqlf()
    def test():
        """ select 1 as one; """

    assert test is not None
    assert isinstance(test, types.FunctionType)


def test_sql_function_yields_generator():

    @sqlf.sqlf()
    def test():
        """ select 1 as one; """

    tmp = test()
    assert tmp is not None
    assert isinstance(tmp, types.GeneratorType)


@pytest.mark.parametrize("value", [(1, 3.14, "", b"", None, [], {})])
def test_sqlf_decorator_takes_function(value):
    with pytest.raises(TypeError):
        sqlf.sqlf(value)


###############################################################################
# sqlf.single_row
###############################################################################


@pytest.mark.parametrize("value", [1, 3.14, "", b"", None, [], {}])
def test_single_row_takes_generator_function(value):

    def it():
        yield {"one": 1}

    with pytest.raises(TypeError):
        sqlf.single_row(value)
    assert sqlf.single_row(it)() is not None


def test_single_row_returns_first_row():

    def it():
        yield {"one": 1}
        yield {"two": 2}

    val = sqlf.single_row(it)()
    assert "one" in val
    assert val["one"] == 1


###############################################################################
# sqlf.single_value
###############################################################################


@pytest.mark.parametrize("value", [1, 3.14, "", b"", None, [], {}])
def test_single_value_takes_generator_function(value):

    def it():
        yield {"one": 1}

    with pytest.raises(TypeError):
        sqlf.single_value(value)
    assert sqlf.single_value(it)() is not None


def test_single_value_returns_first_value_from_first_row():

    def it():
        yield {"one": 1}
        yield {"two": 2}

    val = sqlf.single_value(it)()
    assert val == 1


###############################################################################
# sqlf.as_type
###############################################################################


def test_as_type():

    @sqlf.as_type(lambda **kw: tuple(kw.keys()))
    @sqlf.sqlf()
    def _test():
        """ select 3.14 as pi, 11 as eleven; """

    tmp = list(_test())[0]
    assert len(tmp) == 2
    assert "pi" in tmp
    assert "eleven" in tmp
