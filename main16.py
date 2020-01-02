person = {"name":"Elwing","height":175,"handsome":True}
print(person)

#取出東西: print(name)
print(person["name"])

#新增一個名字: weight = 75
person["weight"] = 75
print(person)

#更改名字背後的值: height = 177
person["height"] = 177
print(person)

#取出來做完運算設定回去: height = height +3
person["height"] = person["height"] + 3
print(person)

#(以前沒有) 刪除
del person["weight"]
print(person)

#for 單個東西暫時名字 in 群集
#{名字:資料} ->因為有兩個, 做出取捨之後, 丟名字給你
for key in person:
    print("-",key,person[key])