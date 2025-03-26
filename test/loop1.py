#Print all key names in the dictionary, one by one
thisdict = {
    "Son": "Saad",
    "Year": 1996,
    "Work": "Logent"
}
for x in thisdict:
    (x)

#Print all values in the dictionary, one by one
thisdict = {
    "Son": "Saad",
    "Year": 1996,
    "Work": "Logent"
}

for x in thisdict:
    (thisdict[x])

#You can also use the values() method to return values of a dictionary
thisdict = {
    "Son": "Saad",
    "Year": 1996,
    "Work": "Logent"
}

for x in thisdict.values():
    (x)
#You can use the keys() method to return the keys of a dictionary
thisdict = {
    "Son": "Saad",
    "Year": 1996,
    "Work": "Logent"
}

for x in thisdict.keys():
    (x)
#Loop through both keys and values, by using the items() method
thisdict = {
    "Son": "Saad",
    "Year": 1996,
    "Work": "Logent"
}

for x, y in thisdict.items():
    (x,y)

x = {'type' : 'fruit', 'name' : 'apple'}

for y in x.values():
    print(y)
