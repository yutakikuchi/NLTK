#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re,pprint,nltk
from nltk.corpus.reader import *
from nltk.corpus.reader.util import *
from nltk.corpus.util import *
from nltk.text import Text

def pp(obj):
    pp = pprint.PrettyPrinter(indent=4, width=160)
    str = pp.pformat(obj)
    return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1),16)), str)

def _knbc_fileids_sort(x):
    cells = x.split('-')
    return (cells[0], int(cells[1]), int(cells[2]), int(cells[3]))

root = nltk.data.find('corpora/knbc/corpus1')
fileids = [f for f in find_corpus_fileids(FileSystemPathPointer(root), ".*") if re.search(r"\d\-\d\-[\d]+\-[\d]+", f)]
knbc = LazyCorpusLoader('knbc/corpus1', KNBCorpusReader, sorted(fileids, key=_knbc_fileids_sort), encoding='euc-jp')
print '/'.join( knbc.words()[:100] )
print '\n\n'.join( '%s' % tree for tree in knbc.parsed_sents()[0:2] )
print '\n'.join( ' '.join("%s/%s"%(w[0], w[1].split(' ')[2]) for w in sent) for sent in knbc.tagged_sents()[0:20] ) 

#print "words :", pp(knbc.words()[:200])
#print "parsed_sents :", str(knbc.parsed_sents()[0])
#print "tagged_words :", pp(knbc.tagged_words()[:5])
