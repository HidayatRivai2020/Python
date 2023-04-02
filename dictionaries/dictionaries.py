# declaration
members = {"leader":"Jack", "fighter":"Night", "defender": "Harry", "support": "Stu"}
print("member= {}".format(members))
print("leader= {}".format(members["leader"]))
print("fighter= {}".format(members["fighter"]))
print("defender= {}".format(members["defender"]))
print("support= {}".format(members["support"]))

#adding new pairs
members["initiator"] = "Beast"
print("member= {}".format(members))
print("initiator= {}".format(members["initiator"]))

#updating pairs
members["initiator"] = "Jack"
members["leader"] = "Captain"
print("member= {}".format(members))
print("initiator= {}".format(members["initiator"]))
print("leader= {}".format(members["leader"]))

#list as value
score = {"leader":[1,3,1], "fighter":[5,8,1], "defender": [2,5,9], "support": [4,3,2]}
print("score= {}".format(score))
print("defender= {}".format(score["defender"]))
print("win= {}".format(score["defender"][0]))
print("tie= {}".format(score["defender"][1]))
print("lose= {}".format(score["defender"][2]))
