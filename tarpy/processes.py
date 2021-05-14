# -*- coding: utf-8 -*-

''' Processes of Tarpy
'''

import bz2
import gzip
import lzma
import shutil


class Compression:
    ''' Compression Handler
    '''
    def __init__(self, mode: str, path: str, compresslevel: int = 9) -> None:
        ...


def comp():
    with open('test.txt', 'rb') as f:
        with gzip.open('test.txt.gz', 'wb') as fc:
            shutil.copyfileobj(f, fc)



comp()
