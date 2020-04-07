s = "I am an NLPer"

def get_bi_gram(target, n=2):
    return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]
        
words = s.split()

print(get_bi_gram(words))
print(get_bi_gram(s))
