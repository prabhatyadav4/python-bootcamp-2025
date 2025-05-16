s = "hello world"       #Strings are immutable

# s[0] = "R"    -> We can't do this.

a = len(s)
print(a)

print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())

# Removing Whitespaces

text = "    Hello World     "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# Finding and Replacing

txt = "Python is fun"
print(txt.find("is"))
print(txt.replace("fun", "awesome"))


# Splitting and Joining

fruits = "Apple,Banana,Litchi"
print(fruits.split(","))
print("," .join(['Apple', 'Banana', 'Litchi']))

# Checking String Properties

data = "Python143"
print(data.isalpha())
print(data.isnumeric())
print(data.isdigit())
print(data.isalnum())
print(data.isspace())
print(data.isascii())