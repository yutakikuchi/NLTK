#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import cJuman 
cJuman.init(['-B', '-e2'])

#JUMANはEUC-JPにしか対応していない
data = open( './madmagi_corpus-euc.txt', ).readlines()
print cJuman.parse_opt(data, cJuman.SKIP_NO_RESULT).decode( 'euc-jp' )
