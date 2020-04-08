import json

with open('jawiki-country.json', 'r') as f:
    l_strip = [s.strip() for s in f.readlines()]

for l in l_strip:
    print(json.loads(l)["category"])
