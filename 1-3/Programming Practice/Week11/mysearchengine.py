import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import shelve
from django.utils.encoding import smart_str

# Create a list of words to ignore
ignorewords = set(['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it'])


class Crawler:
    # Initialize the crawler with the name of database tabs
    def __init__(self, dbtables):
        self.dbtables = dbtables

    def __del__(self):
        self.close()

    def close(self):
        if hasattr(self, 'urllist'): self.urllist.close()
        if hasattr(self, 'wordlocation'): self.wordlocation.close()
        if hasattr(self, 'link'): self.link.close()
        if hasattr(self, 'linkwords'): self.linkwords.close()
        if hasattr(self, 'pagerank'): self.pagerank.close()

    # Index an individual page
    def addtoindex(self, url, soup):
        if self.isindexed(url):
            print('skip', url + ' already indexed')
            return False

        print('Indexing ' + url)
        url = smart_str(url)
        # Get the individual words
        text = self.gettextonly(soup)
        words = self.separatewords(text)

        # Record each word found on this page
        for i in range(len(words)):
            word = smart_str(words[i])

            if word in ignorewords:
                continue

            self.wordlocation.setdefault(word, {})

            self.wordlocation[word].setdefault(url, [])
            self.wordlocation[word][url].append(i)

        return True

    # Extract the text from an HTML page (no tags)
    def gettextonly(self, soup):
        v = soup.string
        if v == None:
            c = soup.contents
            resulttext = ''
            for t in c:
                subtext = self.gettextonly(t)
                resulttext += subtext + '\n'
            return resulttext
        else:
            return v.strip()

    # Separate the words by any non-whitespace character
    def separatewords(self, text):
        splitter = re.compile('\\W+')
        return [s.lower() for s in splitter.split(text) if s != '']

    # Return true if this url is already indexed
    def isindexed(self, url):
        # urllist = {url:outgoing_link_count}
        if smart_str(url) not in self.urllist:
            return False
        else:
            return True


    # Add a link between two pages
    def addlinkref(self, urlFrom, urlTo, linkText):
        fromUrl = smart_str(urlFrom)
        toUrl = smart_str(urlTo)

        if fromUrl == toUrl: return False

        # if not self.link.has_key(toUrl):
        #     self.link[toUrl] = {}

        self.link.setdefault(toUrl, {})
        self.link[toUrl][fromUrl] = None

        words=self.separatewords(linkText)
        for word in words:
            word = smart_str(word)

            if word in ignorewords: continue

            self.linkwords.setdefault(word, [])

            self.linkwords[word].append((fromUrl, toUrl))

        return True

    # Starting with a list of pages, do a breadth
    # first search to the given depth, indexing pages
    # as we go
    def crawl(self, pages, depth=2):
        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    r = requests.get(page)
                except:
                    print("Could not open %s" % page)
                    continue
                soup = BeautifulSoup(r.content, 'html.parser')
                added = self.addtoindex(page, soup)

                if not added:
                    continue

                outgoingLinkCount = 0
                links = soup('a')
                for link in links:
                    if 'href' in link.attrs:
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1:
                            continue
                            # The fragment identifier introduced
                            # by a hash mark (#) is the optional last
                            # part of a URL for a document. It is typically
                            # used to identify a portion of that document.
                        url = url.split('#')[0]  # remove location portion
                        if url[0:4] == 'http' and not self.isindexed(url):
                            newpages.add(url)
                        linkText = self.gettextonly(link)
                        added = self.addlinkref(page, url, linkText)
                        if added:
                            outgoingLinkCount += 1

                self.urllist[smart_str(page)] = outgoingLinkCount
            pages = newpages


    # Create the database tables
    def createindextables(self):
        # {url:outgoing_link_count}
        self.urllist = shelve.open(self.dbtables['urllist'], writeback=True, flag='c')

        #{word:{url:[loc1, loc2, ..., locN]}}
        self.wordlocation = shelve.open(self.dbtables['wordlocation'], writeback=True, flag='c')

        #{tourl:{fromUrl:None}}
        self.link = shelve.open(self.dbtables['link'], writeback=True, flag='c')

        #{word:[(urlFrom, urlTo), (urlFrom, urlTo), ..., (urlFrom, urlTo)]}
        self.linkwords = shelve.open(self.dbtables['linkwords'], writeback=True, flag='c')

    def calculatepagerank(self,iterations=20):
        # clear out the current page rank table
        # {url:pagerank_score}
        self.pagerank = shelve.open(self.dbtables['pagerank'], writeback=True, flag='n')

        # initialize every url with a page rank of 1
        for url in self.urllist:
            self.pagerank[url] = 1.0

        for i in range(iterations):
            print("Iteration %d" % (i))
            for url in self.urllist:
              pr=0.15
              # Loop through all the pages that link to this one
              for linker in self.link[url]:
                  linkingpr = self.pagerank[urlFrom]

                  # Get the total number of links from the linker
                  linkingcount = self.urllist[linker]
                  pr += 0.85*(linkingpr/linkingcount)

            self.pagerank[url] = pr


class searcher:
    def __init__(self,dbtables):
        self.dbtables = dbtables
        self.opendb()

    def __del__(self):
        self.close()

    def close(self):
        if hasattr(self, 'urllist'): self.urllist.close()
        if hasattr(self, 'wordlocation'): self.wordlocation.close()
        if hasattr(self, 'link'): self.link.close()
        if hasattr(self, 'linkwords'): self.linkwords.close()
        if hasattr(self, 'pagerank'): self.pagerank.close()

    def getmatchingpages(self,q):
        results = {}
        # Split the words by spaces
        words = [smart_str(word) for word in q.split()]
        if words[0] not in self.wordlocation:
                return results, words

        url_set = set(self.wordlocation[words[0]].keys())

        for word in words[1:]:
            if word not in self.wordlocation:
                return results, words
            url_set = url_set.intersection(self.wordlocation[word].keys())

        for url in url_set:
            results[url] = []
            for word in words:
                results[url].append(self.wordlocation[word][url])

        return results, words

    def getscoredlist(self, results, words):
        totalscores = dict([(url, 0) for url in results])

        # This is where you'll later put the scoring functions
        weights = []

        # word frequency scoring
        # weights = [(1.0, self.frequencyscore(results))]
                   # (1.0, self.locationscore(results)),
                   # (1.0, self.inboundlinkscore(results))]

        for (weight,scores) in weights:
            for url in totalscores:
                totalscores[url] += weight*scores.get(url, 0)

        return totalscores

    def query(self,q):
        results, words = self.getmatchingpages(q)
        if len(results) == 0:
            print('No matching pages found!')
            return

        scores = self.getscoredlist(results,words)
        rankedscores = sorted([(score,url) for (url,score) in scores.items()],reverse=1)
        for (score,url) in rankedscores[0:10]:
            print('%f\t%s' % (score,url))

    def normalizescores(self,scores,smallIsBetter=0):
        vsmall = 0.00001 # Avoid division by zero errors
        if smallIsBetter:
            minscore=min(scores.values())
            minscore=max(minscore, vsmall)
            return dict([(u,float(minscore)/max(vsmall,l)) for (u,l) \
                         in scores.items()])
        else:
            maxscore = max(scores.values())
            if maxscore == 0:
                maxscore = vsmall
            return dict([(u,float(c)/maxscore) for (u,c) in scores.items()])

    def frequencyscore(self, results):
        counts = {}
        for url in results:
            score = 1
            for wordlocations in results[url]:
                score *= len(wordlocations)
            counts[url] = score
        return self.normalizescores(counts, smallIsBetter=False)

    def locationscore(self, results):
        locations=dict([(url, 1000000) for url in results])
        for url in results:
            score = 0
            for wordlocations in results[url]:
                score += min(wordlocations)
            locations[url] = score
        return self.normalizescores(locations, smallIsBetter=True)

    # def distancescore(self,rows):
    #     # If there's only one word, everyone wins!
    #     if len(rows[0]) <= 2:
    #         return dict([(row[0],1.0) for row in rows])
    #
    #     # Initialize the dictionary with large values
    #     mindistance=dict([(row[0],1000000) for row in rows])
    #
    #     for row in rows:
    #         dist=sum([abs(row[i]-row[i-1]) for i in range(2,len(row))])
    #         if dist < mindistance[row[0]]:
    #             mindistance[row[0]]=dist
    #
    #     return self.normalizescores(mindistance,smallIsBetter=1)

    def inboundlinkscore(self, results):
        inboundcount=dict([(url, len(self.link[url])) for url in results if url in self.link])
        return self.normalizescores(inboundcount)

    def pagerankscore(self, results):
        pageranks = dict([(url, self.pagerank[url]) for url in results])
        maxrank = max(self.pageranks.values())
        normalizedscores = dict([(url,float(score)/maxrank) for (url,score) in self.pagerank.items()])
        return normalizedscores

    def linktextscore(self, results, words):
        linkscores = dict([(url, 0) for url in results.keys()])
        for word in words:
            for (from_url,to_url) in self.linkwords[word]:
                if to_url in linkscores:
                    pr = self.pagerank[from_url]
                    linkscores[to_url] += pr
        maxscore = max(linkscores.values())
        normalizedscores = dict([(url, float(score)/maxscore) for (url, score) in linkscores.items()])
        return normalizedscores

    # Open the database tables
    def opendb(self):
        # {url:outgoing_link_count}
        self.urllist = shelve.open(self.dbtables['urllist'], flag='r')
        #{word:{url:[loc1, loc2, ..., locN]}}
        self.wordlocation = shelve.open(self.dbtables['wordlocation'], flag='r')
        #{tourl:{fromUrl:None}}
        self.link = shelve.open(self.dbtables['link'], flag='r')
        #{word:[(urlFrom, urlTo), (urlFrom, urlTo), ..., (urlFrom, urlTo)]}
        self.linkwords = shelve.open(self.dbtables['linkwords'], flag='r')

