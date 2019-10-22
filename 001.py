# Prepare my_utils.py file

from collections import Counter # Super useful


# download data from project gutenberg
import urllib.request
request = urllib.request.Request('https://www.gutenberg.org/files/219/219-0.txt')
response = urllib.request.urlopen(request)
data = response.read().decode('utf-8')

# How many letters are there
# How many words are there
# What are the ten most common words and how many times are they used?
# Plot a historgrapm of the top 100 words



# String Manipulation functions

# Lower case
# Remove punctuation
# Wrap lines

# What words follow what words?

# What words co-occur in the same sentence?

# Represnt as bag of words?




# Who are the main Characters?


