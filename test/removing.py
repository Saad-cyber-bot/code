#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
    "Son": "Saad",
    "Year": 1996,
    "Work": "Speditør"
}

thisdict.popitem ()

#The del keyword removes the item with the specified key name
x = {"Son": "Saad",
     "Year": 1996,
     "Work": "Speditør"
}

del x["Son"]

#The del keyword can also delete the dictionary completely:
ø = {"Son": "Saad",
     "Year": 1996,
     "Work": "Speditør"
}

del ø

#The clear() method empties the dictionary:
y = {"Son": "Saad",
     "Year": 1996,
     "Work": "Speditør"
}

y.clear()
print(y)

myvar = {'type' : 'fruit', 'name' : 'apple', 'color' : 'red'}
del myvar('color')
print(myvar)
