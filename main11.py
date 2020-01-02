times = 0
#一個記憶區
result = 0
end = 5000
#加到 > 5000才停, 你最後加的數字是多少
while result <= end:
    result = result + (times+ 1)
    times = times + 1
print("最後加數字是",times)