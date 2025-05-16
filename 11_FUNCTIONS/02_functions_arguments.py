# 1.Positional Arguments

def add(a, b):
    return a+b

print(add(5,3))

# 2.Default Arguments

def add(a, b, plus = 0):
    x = a + b + plus
    return x

print(add(4,5))
print(add(5,8,6))

# 3.Keyword Arguments

def add(a,b):
    x = a + b
    return x
print(add(b=4, a=1))