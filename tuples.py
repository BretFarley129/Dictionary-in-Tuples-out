# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

#function will take in a dictionary (d) and lock the key to the value. 
#it will output a list of these tuples
def lock(d):
    myList = []
    for i in d:
        myTuple = (i, d[i])
        myList.append(myTuple)
    return myList

print lock(my_dict)
