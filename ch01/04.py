s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s = s.replace(".", "")

def sub(n):
    return n-1
 
words = s.split()

l = [1, 5, 6, 7, 8, 9, 15, 16, 19]

l2 =[]
for m in l:
  l2.append(m-1)  

d = {}

for w in range(len(words)):
    if w in l2:
        out = words[w][0]
    else:
        out = words[w][0] + words[w][1]

    d[out] = w

print(d)
        
