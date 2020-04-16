import re


class Morph:
    def __init__(self, line):
        # 区切り文字
        separator = re.compile('\t|,')

        # タブとカンマで分割
        cols = separator.split(line)

        self.surface = cols[0]  # 表層形(surface)
        self.base = cols[7]    # 基本形(base)
        self.pos = cols[1]     # 品詞(pos)
        self.pos1 = cols[2]    # 品詞細分類1(pos1)


class Chunk:
    def __init__(self, morphs, dst):

        self.morphs = morphs
        self.srcs = []   # 係り元文節インデックス番号のリスト
        self.dst = dst  # 係り先文節インデックス番号
        self.phrase = ''.join([morph.surface for morph in morphs])  # 文節


morphs = []       # 形態素解析結果の配列
chunks = []       # 係り受け結果の配列
sentences = []  # 1文ごとの配列

"""
例：
* 2 -1D 0/2 0.000000
猫	名詞,一般,*,*,*,*,猫,ネコ,ネコ
で	助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ
ある	助動詞,*,*,*,五段・ラ行アル,基本形,ある,アル,アル
。	記号,句点,*,*,*,*,。,。,。
EOS
"""

exclude = re.compile(r'''(?:\*\s[0-9]+\s) # キャプチャ対象外
                                    (-?\d+)                       # 数字(係り先) =>  -1D 0/2 0.000000　だけ抽出
                                      ''', re.VERBOSE)      # 改行・コメント・空白無視


with open('./neko.txt.cabocha') as f:

    for line in f:
        excluded = exclude.match(line)

        # EOSまたは係り受け解析結果でない場合 => 形態素解析結果
        if not (line == 'EOS\n' or excluded):
            morphs.append(Morph(line))

        # EOSまたは係り受け解析結果で、形態素解析結果がある場合 => Chunkに追加 + morphを初期化
        elif len(morphs) > 0:
            chunks.append(Chunk(morphs, dst))
            morphs = []

        # 係り受け結果の場合
        if excluded:
            dst = int(excluded.group(1))

        # EOSで係り受け結果がある場合
        if line == 'EOS\n' and len(chunks) > 0:
            # 係り元を代入
            for i, chunk in enumerate(chunks):
                if chunk.dst != -1:
                    chunks[chunk.dst].srcs.append(i)
            sentences.append(chunks)
            chunks = []

for si, sentence in enumerate(sentences):
    print('-----', si, '-----')
    for ci, chunk in enumerate(sentence):
        if chunk.dst != -1 and chunk.morphs[0].pos != "記号":
            print('{}:{}\t{}'.format(
                ci, chunk.phrase, sentence[chunk.dst].phrase))

    if si > 3:
        break
