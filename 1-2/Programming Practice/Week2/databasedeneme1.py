import anydbm
import pickle

db = anydbm.open("grades", "c")

grades = ["A", 100]

db["Ahmet"] = pickle.dumps(grades)
db["Mehmet"] = pickle.dumps(["B", 75])

print pickle.loads(db["Mehmet"])

def avg():
    sumgrades = 0
    for i in db.keys():
        sumgrades += pickle.loads(db[i])[1]
    return sumgrades / len(db.keys())

print "Average grade is %f" % avg()
db.close()

