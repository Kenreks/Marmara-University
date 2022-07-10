import os, re

class LibrarySearcher():
    def __init__(self):
        self.wordlocation = self.word_location_dictionary_creator()
        self.searcher()
        
    def word_location_dictionary_creator(self):
        print("Building the index...")
        self.id_title_dictionary = dict()                               #This dictionary is for converting from id to
                                                                        # title name.
        wordlocations = dict()                                          #This is for indexing.It is a nested dictionary

        for i in os.listdir(os.curdir):
            if i == "metadata":                                         #Finding the directory named as metadata
                os.chdir(i)                                             #Going inside of the metadata directory
                break

        for i in os.listdir(os.curdir):                                 #Looking for all the pages
            open_file = open(i)                                         
            read = open_file.read()
            open_file.close()                                           #Closing each page
            
            first_split = read.split('\\\\')                            #It splits from lines with \\.
            abstract_part = first_split[len(first_split)-2]             #Last element of list is just '', and
                                                                        #last second element is always abstract.

            id_of_book = first_split[1].split('/')[1].split('\n')[0]    #Id is always in the line start with 'Paper'
                                                                        #which is in the second element of list
                                                                        #We need extra 2 split to get id.
            second_split = read.split('\n\n')                           #It splits from lines with nothing.
            third_split = second_split[1].split("Author")               #This split for getting the part with starting
                                                                        # with 'Title:'
            title_of_paper = third_split[0]
            title_of_paper = title_of_paper.split('Title:')             #Get rid of 'Title:',prufying the name of title.
            del title_of_paper[0]
            title_of_paper = ''.join(title_of_paper)
            title_of_paper = title_of_paper.split('\n')                 #Some titles can be with more than one line.
            title_of_paper = "".join(title_of_paper)

            
            words_in_title = [word for word in title_of_paper.split(' ') if word != '' and word!='\n']
            words_in_abstract = [word for word in abstract_part.split(' ') if word != '' and word!='\n']

            all_words_in_list = words_in_title + words_in_abstract
                
            self.id_title_dictionary[id_of_book] = title_of_paper        #Getting Each id's title.
            
            for i in range(len(all_words_in_list)):                      #To get indexes of word.
                wordlocations.setdefault(all_words_in_list[i], {}) #The keys of dictionary are words,values are dict.
                wordlocations[all_words_in_list[i]].setdefault(id_of_book, [])
                                                                         #keys are the id and values are indexes.
                wordlocations[all_words_in_list[i]][id_of_book].append(i)

        return wordlocations

    def separatewords(self,text):                                        #The same function in mysearchengine.
        splitter=re.compile('\\W*')
        return [s.lower() for s in splitter.split(text) if s!='']

        
    def normalizescores(self,scores,smallIsBetter=0):           #The same function in mysearchengine.
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

    def getmatchingpapapers(self, q):  #The same function in mysearchengine.
        results = {}
        
        words = [word.lower() for word in q.split() if word.strip() != '']

        if words[0] not in self.wordlocation:
            return results, words

        paper_set = set(self.wordlocation[words[0]].keys())

        for word in words[1:]:
            if word not in self.wordlocation:
                return results, words
            paper_set = paper_set.intersection(self.wordlocation[word].keys()) 

        for paper in paper_set:
            results[paper] = []
            for word in words:
                results[paper].append(self.wordlocation[word][paper])
        return results, words
    
    def frequencyscore(self, results):  #The same function in mysearchengine.
        counts = {}
        for paper in results:
            score = 1
            for wordlocations in results[paper]:
                score *= len(wordlocations)
            counts[paper] = score
        return self.normalizescores(counts, smallIsBetter=False)
    
    def searcher(self):
        while(True):
            search_terms = input('Please enter your search terms: ')
            if search_terms.strip() == 'q':
                break
            
            results, words = self.getmatchingpapapers(search_terms)
            if len(results) == 0:
                print('No matching papers found!')
                continue
            
            scores = self.frequencyscore(results)
            rankedscores = sorted([(score, paper) for (paper,score) in scores.items()],reverse=1)
            counter = 1
            for (score,paper) in rankedscores[0:10]:
                print('%d. %f\t%s' % (counter,score,self.id_title_dictionary[paper]))
                counter += 1

app = LibrarySearcher()
