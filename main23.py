def add(n1,n2):
    return n1 + n2

print(add(3,5))
print(add("hello","abc"))
# print(add("hello", 3))
# print(add(3))
# print(add(3, 5 , 5))

# 不定參數
def  add_multiple(*nlist):
    result = 0
    for n in nlist:
        result = result + n
    return result
print(add_multiple(3,5,6,7))

