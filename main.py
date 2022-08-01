import requests
from util import filter_images

url = 'https://www.vecteezy.com/free-photos'
req = requests.get(url)

response_str = req.text

# retrieving starting index of all img tags
start_indexes = [index for index in range(len(response_str)) if response_str.startswith('<img', index)]

for i in start_indexes:
    # skipping '<img characters
    c = i + 4
    filter_images(response_str, c)

print('Total {} image src'.format(len(start_indexes)))
