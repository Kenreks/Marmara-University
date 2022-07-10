# -*- coding: utf-8 -*-
__author__ = 'alicakmak'

import mysearchengine
reload(mysearchengine)

dbtables = {'urllist': 'urllist.db', 'wordlocation':'wordlocation.db',
            'link':'link.db', 'linkwords':'linkwords.db', 'pagerank':'pagerank.db'}

searcher = mysearchengine.searcher(dbtables)

query = 'privacy' #people

print "Without ranking:"
searcher.query(query, searcher.NORANK)

print "With ranking:"
searcher.query(query, searcher.ALL)



















#searcher.query(u'şehir üniversitesi')
