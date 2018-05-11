""" This is an example of how sqlf can be used.
"""
import base58
import cbor2
import hashlib
import sqlf


class kt_repository(object):

    @sqlf.sqlf(single=True)
    def add(self, obj):
        '''
            INSERT OR IGNORE INTO artefact VALUES (:aid, :data);
            SELECT :aid;
        '''
        data = cbor2.dumps(obj)
        aid = base58.encode(hashlib.sha3_256(data))

        yield 'data', data
        yield 'aid', aid

    @sqlf.sqlf(single=True, default=None)
    def get(self, aid):
        '''
            SELECT data FROM artefact WHERE aid IS :aid;
        '''
        pass

    @sqlf.sqlf(chain=True)
    def __iter__(self):
        """
            SELECT aid FROM artefact ORDER BY local_id;
        """
        pass
