Logent = {
    "Employ1" : {
        "name": "Saad",
        "Year": 1996
        },
    "Employ2": { 
        "name": "Remi",
        "Year": 1993 
},
    "Employ3": {
        "name": "Niklas",
        "Year": 2023
}
}
print()

Employ1 = {
  "name" : "Saad",
  "year" : 2004
}
Employ2 = {
  "name" : "Remi",
  "year" : 2007
}
Employ3 = {
  "name" : "Niklas",
  "year" : 2011
}

Logent = {
  "Employ1" : Employ1,
  "Employ2" : Employ2,
  "Employ3" : Employ3
}

for x, obj in Logent.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

(Logent["Employ3"]["year"])