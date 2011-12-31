#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import nltk
from nltk.corpus.reader import *
from nltk.corpus.reader.util import *
from nltk.text import Text

import matplotlib.pyplot as plt
import pylab
import matplotlib.font_manager as fm

jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^　「」！？。]*[！？。]')
jp_chartype_tokenizer = nltk.RegexpTokenizer(u'([ぁ-んー]+|[ァ-ンー]+|[\u4e00-\u9FFF]+|[^ぁ-んァ-ンー\u4e00-\u9FFF]+)')
data = PlaintextCorpusReader( './', r'madmagi_corpus.txt',
                              encoding='utf-8',
                              para_block_reader=read_line_block,
                              sent_tokenizer=jp_sent_tokenizer,
                              word_tokenizer=jp_chartype_tokenizer )
node = {}
for i in data.words():
    if node.get(i) is not None:
        node[i] = node[i] + 1
    else:
        node[i] = 1
for k,v in sorted( node.items(), key=lambda x:x[1] ):
    print 'word:'+ k, ' count:' + str(v)
