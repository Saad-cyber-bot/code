thisdict = {
    "Son": "Saad",
    "Year": 1996,
    "Work": "Speditør"
}
thisdict.update({"year": 30})
print(thisdict)

#Keys er navn på selve produkt
thisdict.keys()

#Values er navn på produktene
thisdict.values()

x = thisdict.get("Son")

print(x)

x = {'type' : 'fruit', 'name' : 'banana'}

x.update({"name": 'Apple'})

print(x)

thisdict = {
    "Son": "Saad",
    "Year": 1996,
    "Work": "Speditør"
}
thisdict.update({"Name": "Suadad"})
thisdict["Name"] = "Suadad"
print(thisdict)