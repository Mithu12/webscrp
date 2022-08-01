import requests
from Util import Util

web_urls = [
    'https://www.vecteezy.com/free-photos'
]
search_tags = [
    'squirrel', 'John', 'riding', 'aurora'
]
req = requests.get(web_urls[0])

response_str = req.text

# retrieving starting index of all img tags
start_indexes = [index for index in range(len(response_str)) if response_str.startswith('<img', index)]
search_helper = Util(response_str, search_tags)
for i in start_indexes:
    # skipping '<img' characters
    c = i + 4
    search_helper.filter_images(c)
print('Total {} images found'.format(search_helper.count))
