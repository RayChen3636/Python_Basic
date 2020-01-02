name_list = ["Elwing","Amy","Carol"]
print(name_list)

b = name_list.insert(1,"Carol")
print(name_list)
print(b)

#絕對不能做
#name_list = name_list.insert(1,"Carol")
#print(name_list[0])

name_list.remove("Carol")
print(name_list)
del name_list[1]
print(name_list)