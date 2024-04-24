import json
file = open('ex5.json', 'r')
dessert = json.load(file)
file.close()  
for donut in dessert:
    if donut["name"] == "Old Fashioned":
        donut["batters"]["batter"].append({"id": "5001", "type": "Tea"})
        break

file = open('ex5.json', 'w')
json.dump(dessert, file, indent=4)
file.close()  
