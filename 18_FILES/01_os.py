import os

# List all files and directories in the specified path
a = os.listdir("dir")
print(a)

# Print the current working directory
print(os.getcwd())

# Check if the specified path exists
print(os.path.exists("dir"))

# Remove the file named "sample.txt"
os.remove("sample.txt")

# Remove the directory named "dir" (commented out)
# os.rmdir("dir")