import feedparser
import re


# Strips out all of the HTML and splits the words by nonalphabetical characters
# and returns them as a list.
def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']


# Returns title and dictionary of word counts for an RSS feed
def getwordcounts(url):
    # Parse the feed
    print 'processing ' + url
    d = feedparser.parse(url)
    wc = {}

    # Loop over all the entries
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description

        # Extract a list of words
        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1
    try:
        return d.feed.title, wc
    except AttributeError:
        return None, None

if __name__ == '__main__':
    apcount = {}
    wordcounts = {}
    feedlist = []

    for feedurl in file('feedlist.txt'):
        title, wc = getwordcounts(feedurl)
        if title != None:
            #print '   DONE!'
            feedlist.append(feedurl)
            wordcounts[title] = wc
            for word, count in wc.items():
                apcount.setdefault(word, 0)
                if count > 1:
                    apcount[word] += 1
        else:
            pass
            
    wordlist = []
    for w, bc in apcount.items():
        frac = float(bc) / len(feedlist)
        if frac > 0.1 and frac < 0.5:
            wordlist.append(w)

    out = file('blogdata.txt', 'w')
    out.write('Blog')
    for word in wordlist:
        out.write('\t%s' % word)
    out.write('\n')
    for blog, wc in wordcounts.items():
        # incase there are non ascii blog texts
        blog = blog.encode('ascii', 'ignore')
        out.write(blog)
        for word in wordlist:
            if word in wc:
                out.write('\t%d' % wc[word])
            else:
                out.write('\t0')
        out.write('\n')
