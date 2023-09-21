import json
import os
# Load the JSON data into a Python object
json_data = json.load(open('pos_0.png.json'))
json_data2 = json.load(open('pos_10010.png.json'))
json_data3 = json.load(open('pos_10492.png.json'))

my_dictionary = []
my_dictionary.append(json_data)
my_dictionary.append(json_data2)
my_dictionary.append(json_data3)

for dictionary in my_dictionary:
    #print(dictionary)
    objects= dictionary["objects"]
    #print(objects)
    for object in objects:
        if object["classTitle"]== "Vehicle":
            object["classTitle"] = "Car"
        elif object["classTitle"]== "License Plate":
            object["classTitle"] = "Number"
        print(object["classTitle"])

print(my_dictionary)

with open(os.path.join("jsonfiles", "formatted.json"), "w") as output:
    json.dump(my_dictionary, output)


