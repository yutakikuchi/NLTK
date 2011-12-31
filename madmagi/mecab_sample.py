#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import nltk
from nltk.corpus.reader import *
from nltk.corpus.reader.util import *
from nltk.text import Text
from nltk.tokenize.api import *

import MeCab
import jptokenizer

jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^　「」！？。]*[！？。]')
data = PlaintextCorpusReader( './', r'madmagi_corpus.txt',
                              encoding='utf-8',
                              para_block_reader=read_line_block,
                              sent_tokenizer=jp_sent_tokenizer,
                              word_tokenizer=jptokenizer.JPMeCabTokenizer())
print '/' .join( data.words() )
