s1 = "paraparaparadise"
s2 = "paragraph"

def n_gram(target, n=2):
  return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]

x = n_gram(s1)
y = n_gram(s2)

X=set(x)
Y=set(y)

print(X.union(Y))
print(X & Y)
print(X-Y)

if "se" in x:
  print("se is in X")
else:
  print("se isn't in X")
  
if "se" in y:
  print("se is in Y")
else:
  print("se isn't in Y")
