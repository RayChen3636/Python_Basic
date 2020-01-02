import random
prize = set()
while len(prize) < 7:
    n = random.randint(0,48)
    prize.add(n)
print("頭獎彩券:", prize)

times = 0
# 無窮迴圈 + 手動停止(break)
# 使用時機: 當你while條件寫不出來的時候
while True:
    lottery = set()
    while len(lottery) < 7:
        n = random.randint(0, 48)
        lottery.add(n)
    print("我買的彩券:", lottery)
    times = times + 1

    total = 0
    for n in lottery:
        if n in prize:
            print(n,"中了")
            total = total + 1
    print("中了", total , "個數字")

    if total >= 6:
        break
print("總共買了", times ,"張,才中")