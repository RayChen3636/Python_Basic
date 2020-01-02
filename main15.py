import random
win = 0
lose = 0
for times in range(0,10000):
    # 準備三門
    doors = ["羊","羊"]
    c = random.randint(0,2)
    doors.insert(c,"車")
    print(doors)
    # 讓參賽者選一道門
    c = random.randint(0,2)
    print("使用者選的:", doors[c])
    del doors[c]
    print("剩下的門:", doors)
    # 主持人開一隻羊
    doors.remove("羊")
    print("最後剩下的門", doors)
    # 確認一下到底是輸還是贏
    if doors[0] == "車":
        win = win + 1
        print("贏了, 賺")
    else:
        lose = lose + 1
        print("輸了, 虧")
print("贏的次數", win)
print("輸的次數", lose)
total = win + lose
print("贏的機率", win / total * 100 , "%")
print("輸的機率", lose / total * 100, "%")

