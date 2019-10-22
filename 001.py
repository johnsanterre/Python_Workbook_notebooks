# Prepare my_utils.py file

# download data from project gutenberg
import urllib.request
request = urllib.request.Request('https://www.gutenberg.org/files/219/219-0.txt')
response = urllib.request.urlopen(request)
data = response.read().decode('utf-8')


# String Manipulation functions

# Lower case
# Remove punctuation
# Wrap lines

# What words follow what words?

# What words co-occur in the same sentence?

# Represnt as bag of words?




# Who are the main Characters?


