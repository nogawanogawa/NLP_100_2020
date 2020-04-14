import json
import re

with open('jawiki-country.json', 'r') as f:
    l_strip = [s.strip() for s in f.readlines()]

i = json.loads(l_strip[0])["text"]

for section in re.findall(r'(=+)([^=]+)\1\n', i):
    if len(section[0]) > 1:
        print('{}\t{}'.format(section[1].strip(),       # == hoge == でいう "hoge"
                              len(section[0]) - 1))     # == の数
