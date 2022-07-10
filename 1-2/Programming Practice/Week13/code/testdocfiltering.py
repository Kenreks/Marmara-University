__author__ = 'alicakmak'

import docclass
cl = docclass.classifier(docclass.getwords)
cl.train('the quick brown fox jumps over the lazy dog','good')
cl.train('hello there','good')
cl.train('make quick money in the online casino','bad')

print cl.fc
print cl.cc

print cl.fcount('quick','good')
print cl.categories()

print cl.fprob('quick', 'good')