# Traditional approach without using the walrus operator:

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)
# print(foods)

# Using the walrus operator (introduced in Python 3.8) for a more concise approach:
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
print(foods)
