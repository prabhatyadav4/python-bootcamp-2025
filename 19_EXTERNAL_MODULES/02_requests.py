# Import the requests module for making HTTP requests
import requests

# Send a GET request to the specified URL
r = requests.get('https://www.google.com')

# Write the response content to a file
with open("KernalPrab.txt", "w") as f:
    f.write(r.text)