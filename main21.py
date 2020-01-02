person1 = ("Elwing", 175 , 75)
print(person1)

person1 = person1 + ("Taipei",)
print(person1)

print(person1[2])
print(person1[:2])

# tuple刪除? python不希望你做,它沒定義
# (不建議) 可以繞彎達到
print(person1[0:1] + person1[2:])