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
from pylab import *
import matplotlib.font_manager as fm


jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^　「」！？。]*[！？。]')
jp_chartype_tokenizer = nltk.RegexpTokenizer(u'([ぁ-んー]+|[ァ-ンー]+|[\u4e00-\u9FFF]+|[^ぁ-んァ-ンー\u4e00-\u9FFF]+)')
data = PlaintextCorpusReader( './', r'madmagi_corpus.txt',
                              encoding='utf-8',
                              para_block_reader=read_line_block,
                              sent_tokenizer=jp_sent_tokenizer,
                              word_tokenizer=jp_chartype_tokenizer )
fdist = nltk.FreqDist(data.words())
fp = fm.FontProperties(fname='/home/yuta/.fonts/IPAfont00303/ipag.ttf') 
xlabel( u'単語', size='20', fontproperties=fp )
ylabel( u'個数', size='20', fontproperties=fp )
title( u'魔法少女まどか☆マギカの単語数plot', size='20', fontproperties=fp )
fdist.plot()
savefig( 'madmagi_plot.png' )
