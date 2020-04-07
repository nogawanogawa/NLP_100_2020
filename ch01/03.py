s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

s = s.replace('.', '').replace(',', '')
words = s.split()
out = []

for w in words:
    out.append(len(w))

print(out)
