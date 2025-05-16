s = {1,5,2,8,9}

print(s)

s.add(4)
print(s)

s.remove(9)
print(s)

# s.remove(55)        # Throws an error

s.discard(55)       # No error if element not found
print(s)

s.pop()
print(s)