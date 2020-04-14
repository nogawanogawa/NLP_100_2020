import json
import re

with open('jawiki-country.json', 'r') as f:
    l_strip = [s.strip() for s in f.readlines()]

i = json.loads(l_strip[10])["text"]

m1 = re.search(r'{{基礎情報 国.*', i)  # 開始
m2 = re.search(r'(.*)\n}}\n', i[m1.end():])  # 終了
template = i[m1.end():m2.end()+1]
template = template.split("\n")

d = {}
for t in template:
    m = re.match(r'\|(.+) = (.*)', t)
    if m is not None:
        d[m.group(1)] = m.group(2)

print(d)
