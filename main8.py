#逃脫字元: \n:換行 \t:TAB \b: backspace
a = "hello\nhello"
print(a)
print(len(a))

b = "hello\bpython"
print(b)
print(b == "hellpython")
print(len(b))