import requests
import json
import re


def remove_stub(text):
    return re.sub(r"{{(.*)}}", lambda m: m.group(1), text)


def remove_define(text):
    return re.sub(r"^(;|:)\s*", "", text)


def remove_num_itemize(text):
    return re.sub(r"^#+\s*", "", text)


def remove_itemize(text):
    return re.sub(r"^\*+\s*", "", text)


def remove_comment(text):
    return re.sub(r"<!--.*?-->", "", text)


def remove_redirect(text):
    return re.sub(r"#REDIRECT \[\[" +
                  "(" +
                  ".*"
                  ")" +
                  "\]\]",
                  lambda m: m.group(1),
                  text)


def remove_category(text):
    return re.sub(r"\[\[Category:" +
                  ".*" +
                  "\]\]",
                  "",
                  text
                  )


def remove_external_link(text):
    return re.sub(r"\[" +
                  "(" +
                  "[^]]+"
                  ")" +
                  "]",
                  lambda m: m.group(1).split(" ")[-1],  # "|"でスプリットして末尾を取得
                  text
                  )


def remove_file(text):
    return re.sub(r"\[\[ファイル:" +
                  "(" +
                  "[^]]+" +
                  ")" +
                  "\]\]",
                  lambda m: m.group(1).split("|")[-1],  # "|"でスプリットして末尾を取得
                  text)


def remove_internal_link(text):
    return re.sub(r"\[\[" +
                  "(" +
                  "[^]]+" +
                  ")" +
                  "\]\]",
                  lambda m: m.group(1).split("|")[-1],  # "|"でスプリットして末尾を取得
                  text)


def remove_emph(text):
    return re.sub(r'\'\'*', "", text)


with open('jawiki-country.json', 'r') as f:
    l_strip = [s.strip() for s in f.readlines()]

i = json.loads(l_strip[1])["text"]

m1 = re.search(r'{{基礎情報 国.*', i)  # 開始
m2 = re.search(r'(.*)\n}}\n', i[m1.end():])  # 終了
template = i[m1.end():m2.end()+1]
template = template.split("\n")

d = {}
for t in template:
    m = re.match(r'\|(.+) = (.*)', t)
    if m is not None:
        key = re.sub(r'\'\'*', "", m.group(1))
        value = m.group(2)

        value = remove_define(value)
        value = remove_num_itemize(value)
        value = remove_itemize(value)
        value = remove_comment(value)
        value = remove_redirect(value)
        value = remove_category(value)
        value = remove_external_link(value)
        value = remove_internal_link(value)
        value = remove_file(value)
        value = remove_emph(value)
        value = remove_stub(value)

        # 差分
        d[key] = value

S = requests.Session()

URL = "https://www.mediawiki.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:" + d["国旗画像"],
    "iiprop": "url"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    print(v["imageinfo"][0]["url"])
