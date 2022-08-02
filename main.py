import requests
from Util import Util

web_urls = [
    'https://www.vecteezy.com/free-photos',
    'https://burst.shopify.com/',
    'https://www.freeimages.com/',
    'https://kaboompics.com/',
    'https://stocksnap.io/',
    'https://www.lifeofpix.com/',
    'https://gratisography.com/',
]

# an empty string '' as a tag will print all available image sources
search_tags = [
    'squirrel', 'John', 'riding', 'aurora', 'office', 'palm', 'young', 'works', 'woman', 'beach',
]
search_helper = Util('', search_tags)
for url in web_urls:
    req = requests.get(url)
    response_str = req.text

    # replacing the helper class 'response_str' with the response from the request
    search_helper.response_str = response_str
    search_helper.count = 0

    # retrieving starting index of all img tags
    start_indexes = [index for index in range(len(response_str)) if response_str.startswith('<img', index)]

    for i in start_indexes:
        # skipping '<img' characters
        c = i + 4
        search_helper.filter_images(c)
    # print('Total {} images found'.format(search_helper.count))
    print()
