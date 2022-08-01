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
    alt = ''
    while response_str[c] != '>':
        if response_str.startswith('src=', c):
            # skipping 'src="' characters
            srcStart = c + 5
            while response_str[srcStart] != '"':
                src = src + response_str[srcStart]
                srcStart += 1
            print(src)
        if response_str.startswith('alt=', c):
            # skipping 'alt="' characters
            altStart = c + 5
            while response_str[altStart] != '"':
                alt = alt + response_str[altStart]
                altStart += 1
            print(alt)

        c += 1

print('Total {} image src'.format(len(start_indexes)))
