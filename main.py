import requests

url = 'https://www.vecteezy.com/free-photos'
req = requests.get(url)

response_str = req.text

# retrieving starting index of all img tags
start_indexes = [index for index in range(len(response_str)) if response_str.startswith('<img', index)]

for i in start_indexes:
    # skipping '<img characters
    c = i + 4
    src = ''
    while response_str[c] != '>':
        if response_str.startswith('src=', c):
            # skipping 'src="' characters
            srcStart = c + 5
            while response_str[srcStart] != '"':
                src = src + response_str[srcStart]
                srcStart += 1
            print(src)
        c += 1

print('Total {} image src'.format(len(start_indexes)))
