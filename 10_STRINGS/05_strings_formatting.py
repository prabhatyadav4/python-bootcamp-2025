# Strings Formatting

#format()

data = "Hey {}, you have done a great work. Here is your price money worth ${}."

a = "John"
a1 = "10000"
b = "David"
b1 = "1000"
c = "Harry"
c1 = "100"

s1 = data.format(a,a1)
print(s1)
s2 = data.format(b,b1)
print(s2)
s3 = data.format(c,c1)
print(s3)

print("\n")

# f-srings

print(f"Hey {a}, you have done a great work. Here is your price money worth ${a1}.")
print(f"Hey {b}, you have done a great work. Here is your price money worth ${b1}.")
print(f"Hey {c}, you have done a great work. Here is your price money worth ${c1}.")

print("\n")

#Character Encoding

#ord()
print(ord('A'))

#chr()
print(chr(65))