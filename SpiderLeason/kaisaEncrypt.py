from string import ascii_letters,ascii_lowercase,ascii_uppercase

def kaisaEncrypt(text,k):
    #凯撒加密
    lower = ascii_lowercase[k:] + ascii_lowercase[:k]
    upper = ascii_uppercase[k:] + ascii_uppercase[:k]
    table = ''.maketrans(ascii_letters,lower+upper)
    return text.translate(table)

s = "Python is great programming language.I like it!"
print(kaisaEncrypt(s,3))

