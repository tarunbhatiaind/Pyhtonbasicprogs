d1 ={"Harry":"toffee","Tarun":"chai","gaurav":"beer","shubham":{"Lunch":"abc","Dinner":"cde"}}
print(d1["shubham"]["Dinner"])
print(d1)
del d1["Harry"]
print(d1)
d1.update({"Harry":"toffee"})
print(d1.keys())
print(d1.items())
#below is harry video question to get the meaaning of the word from the dictionary
print("QUESTION HARRY")
DICT={"hist":"history","chem":"chemistry","phy":"physics","calc":"calculate"}
print("INSERT THE WORD FOR IT'S MEANING")
word=input()
print("Meaning of your word is :",DICT.get(word))
