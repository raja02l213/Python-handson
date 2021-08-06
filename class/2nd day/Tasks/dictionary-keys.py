"""
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "celcious": -14.4,
  "colors": ["red", "white", "blue"]
}

print(thisdict.keys())
thisdict["reverse-gear"] = True
print(thisdict)
"""
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
print(car.values())

if "model" in car:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")