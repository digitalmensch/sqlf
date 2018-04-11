# -*- coding: utf-8 -*-

''' SQL in F(unctions)

    udf_lib contains useful user-defined functions
'''


import cbor2
import typeguard
import typing


###############################################################################
# Data Serialisation
###############################################################################


def cbor_map() -> bytes:
    return cbor2.dumps(dict())


@typeguard.typechecked
def cbor_insert(obj: bytes, key: typing.Any, value: typing.Any) -> bytes:
    tmp = cbor2.loads(obj)
    tmp[key] = value
    return cbor2.dumps(tmp)


@typeguard.typechecked
def cbor_has(obj: bytes, key: typing.Any) -> bool:
    tmp = cbor2.loads(obj)
    return key in tmp
