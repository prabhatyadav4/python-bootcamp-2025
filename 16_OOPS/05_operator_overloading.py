class Point:
    # Constructor to initialize the x and y coordinates of the point
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Method to calculate the sum of two points and return a new Point object
    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))
    
    # Method to print the coordinates of the point
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")

    # Incorrect implementation of the __add__ method (not used in the current code)
    def __add__(self):
        return Point((self.x + p.x), (self.y + p.y))
    
# Create two Point objects
p1 = Point(2, 4)
p2 = Point(4, 3)

# Calculate the sum of p1 and p2 using the sum method
p = p1.sum(p2)

# Print the coordinates of the resulting point
p.print_point()