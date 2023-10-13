from kaisaEncrypt import *
def check(text):
    # 测试文本总是否存在至少两个最常见的英语单词
    # 列表可扩展，规则可调整
    mostCommonWords = ('the','is','to','not','have','than','for')
    return sum(1 for word in mostCommonWords if word in text) >=2

# 测试
text = "Beautiful is better than ugly"
# 加密
encrptedText = kaisaEncrypt(text,5)
# 暴力破解
for i in range(1,26):
    t = kaisaEncrypt(encrptedText,-i)
    if check(t):
        print(i,t,sep=":")
        break

