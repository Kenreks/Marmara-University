import anydbm
import pickle

db = anydbm.open("grades.txt", "c")

grades = ["B", 100]  # exam grade and attendance

db["Osman"] = pickle.dumps(grades)
db["Ali"] = pickle.dumps(["A", 50])

print pickle.loads(db["Osman"])


def getAvgAtt():
    sumGrades = 0
    # the following code is faster but unfortunately Apple-originated
    # 2.7 interpreter does not recognize db.values(), db.items(), ...
    # for v in db.values():
    #    sum += pickle.loads(v)[1]
    for k in db.keys():
        sumGrades += pickle.loads(db[k])[1]
    return sumGrades / len(db.keys())


print "Average grade is %f" % getAvgAtt()
db.close()
