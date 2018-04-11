# -*- coding: utf-8 -*-

"""Top-level package for SQL in F(unctions)."""

__author__ = """Digitalmensch"""
__email__ = 'contact@digitalmensch.ch'
__version__ = '0.2.8'

from .sqlf import sqlf
from .sqlf import scalar_udf
from .sqlf import single_row
from .sqlf import as_type

# Activate built-in UDFs
from ._udf_text import similar
from ._udf_text import number
from ._udf_encoding import tohex
from ._udf_encoding import b91enc
from ._udf_encoding import b91dec
from ._udf_cryptography import nonce
from ._udf_cryptography import sha3
from ._udf_serialisation import cbor_map
from ._udf_serialisation import cbor_insert
from ._udf_serialisation import cbor_has
scalar_udf(similar)
scalar_udf(number)
scalar_udf(tohex)
scalar_udf(b91enc)
scalar_udf(b91dec)
scalar_udf(nonce)
scalar_udf(sha3)
scalar_udf(cbor_map)
scalar_udf(cbor_insert)
scalar_udf(cbor_has)
del similar, number, tohex, b91enc, b91dec, nonce, sha3, cbor_map, cbor_insert
del cbor_has

__all__ = [
    'sqlf',
    'scalar_udf',
    'single_row',
    'as_type',
]
