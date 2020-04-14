import json
import re

with open('jawiki-country.json', 'r') as f:
    l_strip = [s.strip() for s in f.readlines()]

i = json.loads(l_strip[10])["text"]

lines = i.split("\n")

for line in lines:
    # print(line)
    if re.match(r'\[\[:*(File|ファイル):.*\]\]$', line):
        m = re.match(r'\[\[:*(ファイル|File):(.+?)\|.+\]\]$', line)
        print(m.group(2))
    # pattern 2
    elif re.match(r'^(ファイル|File):.*\]\]$', line):
        m = re.match(r'^(ファイル|File):(.+?)\|.+$', line)
        print(m.group(2))
