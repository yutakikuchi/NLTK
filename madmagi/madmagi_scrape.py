#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,re,urllib,urllib2
urls = ( 'http://www22.atwiki.jp/madoka-magica/pages/170.html', 
         'http://www22.atwiki.jp/madoka-magica/pages/175.html',
         'http://www22.atwiki.jp/madoka-magica/pages/179.html',
         'http://www22.atwiki.jp/madoka-magica/pages/180.html',
         'http://www22.atwiki.jp/madoka-magica/pages/200.html',
         )
f = open( './madmagi_corpus.txt', 'w' )
opener = urllib2.build_opener()
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.51.22 (KHTML, like Gecko) Version/5.1.1 Safari/    534.51.22'
referer = 'http://www22.atwiki.jp/madoka-magica/'
opener.addheaders = [( 'User-Agent', ua ),( 'Referer', referer )]
for url in urls:
    content = opener.open( url ).read()
    if re.compile( r'<div class="contents".*?>((.|\n)*?)</div>', re.M ).search( content ) is not None:
        data = re.compile( r'<div class="contents".*?>((.|\n)*?)</div>', re.M ).search( content ).group()
        if re.compile( r'「(.*?)」', re.M ).search( data ) is not None: 
            lines = re.compile( r'「(.*?)」', re.M ).findall( data )
            for line in lines:
                f.write( line + "\n" )
f.close()
