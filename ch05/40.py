import re

morphs = []  # 形態素解析結果
sentences = []  # 最終的に入れるリスト


class Morph:
    def __init__(self, line):
        # タブかカンマでで区切り
        separator = re.compile('\t|,')

        cols = separator.split(line)

        self.surface = cols[0]
        self.base = cols[7]
        self.pos = cols[1]
        self.pos1 = cols[2]


exclude = re.compile(r'''EOS\n      # EOS, 改行コード
                         |          # OR
                         \*\s\d+\s  # '*, 空白, 数字１つ以上, 空白
                       ''', re.VERBOSE)

with open('./neko.txt.cabocha') as f:

    for line in f:
        if not exclude.match(line):
            morphs.append(Morph(line))
        if line == 'EOS\n' and len(morphs) > 0:
            sentences.append(morphs)
            morphs = []

for sentence in sentences[2]:
    print(sentence.__dict__)
