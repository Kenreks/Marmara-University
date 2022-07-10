critics = {'Claudia Puig': {'Just My Luck': 3.0,
  'Snakes on a Plane': 3.5,
  'Superman Returns': 4.0,
  'The Night Listener': 4.5,
  'You, Me, and Dupree': 2.5},
 'Gene Seymour': {'Just My Luck': 1.5,
  'Lady in the Water': 3.0,
  'Snakes on a Plane': 3.5,
  'Superman Returns': 5.0,
  'The Night Listener': 3.0,
  'You, Me, and Dupree': 3.5},
 'Jack Mathews': {'Lady in the Water': 3.0,
  'Snakes on a Plane': 4.0,
  'Superman Returns': 5.0,
  'The Night Listener': 3.0,
  'You, Me, and Dupree': 3.5},
 'Lisa Rose': {'Just My Luck': 3.0,
  'Lady in the Water': 2.5,
  'Snakes on a Plane': 3.5,
  'Superman Returns': 3.5,
  'The Night Listener': 3.0,
  'You, Me, and Dupree': 2.5},
 'Michael Phillips': {'Lady in the Water': 2.5,
  'Snakes on a Plane': 3.0,
  'Superman Returns': 3.5,
  'The Night Listener': 4.0},
 'Mick LaSalle': {'Just My Luck': 2.0,
  'Lady in the Water': 3.0,
  'Snakes on a Plane': 4.0,
  'Superman Returns': 3.0,
  'The Night Listener': 3.0,
  'You, Me, and Dupree': 2.0},
 'Toby': {'Snakes on a Plane': 4.5,
  'Superman Returns': 4.0,
  'You, Me, and Dupree': 1.0},
 'Ali': {'Just My Luck': 2.0,
  'Snakes on a Plane': 2.5,
  'Superman Returns': 2.5,
  'The Night Listener': 5.0}}

from math import sqrt

def sim_distance(prefs, person1, person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    if len(si)==0: return 0
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item],2)\
                          for item in si])
    return 1/(1+sqrt(sum_of_squares))

def sim_pearson(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1
    n = len(si)
    if n == 0:
        return 0
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    sum1Sq = sum([pow(prefs[p1][it],2) for it in si]) 
    sum2Sq = sum([pow(prefs[p2][it],2) for it in si])
    pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])
    num = pSum-(sum1*sum2/n)
    den = sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den == 0:
        return 0
    return num/den

def topMatches(prefs, person, n=3, similarity=sim_pearson):
    scores = [(round(similarity(prefs,person,other), 2),other) \
              for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

def getRecommendations(prefs, person, similarity = sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        sim = similarity(prefs, person, other)

        if sim <= 0: continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item]*sim
                simSums.setdefault(item, 0)
                simSums[item] += sim
    rankings = [(round(total/simSums[item], 2),item) for item, total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings

def transformPrefs(prefs):
    result = {}
    for person in prefs:
    	for item in prefs[person]:
        	result.setdefault(item, {})
        	result[item][person] = prefs[person][item]
    return result


def calculateSimilarItems(prefs,n=10):
    # Create a dictionary of items showing which other items they
    # are most similar to.
    result={}
    
    # Invert the preference matrix to be item-centric
    itemPrefs=transformPrefs(prefs)
    c=0
    
    for item in itemPrefs:
        # Status updates for large datasets
        c+=1
        if c%100==0: print("%d / %d" % (c,len(itemPrefs)))
        # Find the most similar items to this one
        scores=topMatches(itemPrefs,item,n=n,similarity=sim_distance)
        result[item]=scores

    return result

def getRecommendedItems(prefs,itemMatch,user):
    userRatings=prefs[user]
    scores={}
    totalSim={}

    # Loop over items rated by this user
    for (item,rating) in userRatings.items():
        # Loop over items similar to this one
        for (similarity,item2) in itemMatch[item]:
            # Ignore if this user has already rated this item
            if item2 in userRatings: continue

            # Weighted sum of rating times similarity
            scores.setdefault(item2,0)
            scores[item2]+=similarity*rating

            # Sum of all the similarities
            totalSim.setdefault(item2,0)
            totalSim[item2]+=similarity

    # Divide each total score by total weighting to get an average
    rankings=[(round(score/totalSim[item], 2),item) for item,score in scores.items()]
    # Return the rankings from highest to lowest
    rankings.sort()
    rankings.reverse()
    return rankings
