__author__ = 'alicakmak'

import docclass

cl = docclass.naivebayes(docclass.getwords)

docclass.sampletrain(cl)

print cl.prob('quick rabbit','good')
print cl.prob('quick rabbit','bad')

print cl.prob('quick money','good')
print cl.prob('quick money','bad')

print cl.classify('quick rabbit')
print cl.classify('quick money')


