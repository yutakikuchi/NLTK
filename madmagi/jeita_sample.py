#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import nltk
from nltk.corpus.reader import *
from nltk.corpus.reader.util import *
from nltk.text import Text

jeita = ChasenCorpusReader('/home/yuta/nltk_data/corpora/jeita.zip', '.*chasen', encoding='utf-8')
from nltk.corpus.util import LazyCorpusLoader
jeita = LazyCorpusLoader('jeita', ChasenCorpusReader, r'.*chasen', encoding='utf-8')
print '/'.join( jeita.words()[22100:22140] )

