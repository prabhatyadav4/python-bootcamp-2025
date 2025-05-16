# Regular Expressions (regex) are a sequence of characters that define a search pattern.
# They are used for string matching, searching, and manipulation.

import re

# Sample text to perform regex operations on
text = "The quick brown fox jumps over the lazy dog."

# Search for the word "brown" in the text
match = re.search("brown", text)
print(match)  # Prints the match object if found, otherwise None

if match:
    print("Match Found!")  # Indicates that the word "brown" was found
    print("Start Index: ", match.start())  # Prints the start index of the match
    print("End Index: ", match.end())  # Prints the end index of the match

# Find all occurrences of the word "the" (case-insensitive) in the text
matches = re.findall("the", text, re.IGNORECASE)
print("Matches:", matches)  # Prints a list of all matches

# Replace the word "fox" with "cat" in the text
new_text = re.sub("fox", "cat", text)
print("New Text: ", new_text)  # Prints the modified text