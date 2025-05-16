#  Lambda functions are anonymous, inline functions.

square = lambda x: x*x
"""
As good as writing:
def square(x):
    return x*x
"""

sum = lambda x,y: x+y
"""
As good as writing:
def sum(x,y):
    return x+y
"""

print(square(3))
print(sum(2,5))