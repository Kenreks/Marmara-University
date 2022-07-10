# -*- coding: utf-8 -*-
__author__ = 'alicakmak'

import mysearchengine
#reload(mysearchengine)

dbtables = {'urllist': 'urllist.db', 'wordlocation':'wordlocation.db',
            'link':'link.db', 'linkwords':'linkwords.db', 'pagerank':'pagerank.db'}

crawler=mysearchengine.crawler(dbtables)
crawler.createindextables()

pagelist=['http://cs.sehir.edu.tr/en/profile/13/Ercan-Nergiz/']
crawler.crawl(pagelist, depth=2)





#searcher.query(u'şehir üniversitesi')
