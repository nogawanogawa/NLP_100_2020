import random
text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind "

def change(s):
    out = []
    o = ""
    for word in s:
        if len(word) > 4:
            head = word[0]
            tail = word[-1]
            text = []
            for w in word[1:-2]:
                text.append(w)
            random.shuffle(text)
            text_2= "".join(text)
            o = head + text_2 + tail
        else:
            o = word
        out.append(o)
    return out

temp = text.split()
print(change(temp))
