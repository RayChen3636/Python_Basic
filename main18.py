import jieba
# 第一種import寫法
# import jieba.analyse
# 第二種import寫法
# from jieba import analyse
# 第三種import寫法
from jieba.analyse import extract_tags

# 讀取檔案三部曲
# 1.所有資源放在專案底下
# 2.檔案路徑: 相對路徑
f = open("a.txt","r", encoding="utf-8")
article = f.read()
f.close()

#jieba.load_userdict(".\mydict.txt")
jieba.add_word("蠟像")
jieba.add_word("蠟像館")
jieba.add_word("周杰倫")

# ["詞1", "詞2", "詞3"]
# 我中午吃牛排 -> 我 中午 吃 牛排
sep = " ".join(jieba.cut(article))
print(sep)

print("關鍵詞",extract_tags(article,5))