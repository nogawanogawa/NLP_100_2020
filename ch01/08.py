def cipher(s):
    out = ""
    for t in s:
        if t.islower():
            t_code = ord(t)
            out += chr(219 - t_code)
        else:
            out += t

    return out

s = "This"
s1 = "pen"

print(cipher(s))
print(cipher(s1))
