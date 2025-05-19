import requests
from colorama import Fore, Style, init

# Prompt the user to input the type of news they want to read
query = input("What type of news you want to read? \n")

# API key for the News API
api = "3ee9a4eb73da46b882a531b74d396d1e"

# Construct the URL for the API request
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-03-30&sortBy=publishedAt&apiKey={api}"

# Send a GET request to the News API
r = requests.get(url)

# Parse the JSON response
data = r.json()

# Extract the list of articles from the response
articles = data["articles"]

# Loop through the articles and display their titles and URLs
for index, article in enumerate(articles):
    # Print the article title with styling
    print(Fore.CYAN + Style.BRIGHT + f"{index+1}. {article['title']}")
    # Reset the style and print the article URL
    print(Style.RESET_ALL + article["url"])
    # Print a separator line
    print("\n-------------------------------------------------------------------------------------------------------------------------\n")