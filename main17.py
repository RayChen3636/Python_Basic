# 讀取檔案三部曲
# 1.所有資源放在專案底下
# 2.檔案路徑: 相對路徑
f = open("a.txt","r", encoding="utf-8")
article = f.read()
f.close()

print(article)

result = {}
for c in article:
    if c in result:
        result[c] = result[c] + 1
    else:
        result[c] = 1
print(result)

# 體驗一下jieba
import jieba.analyse
keywords = jieba.analyse.extract_tags(article,5)
print("最關鍵詞:",keywords)

