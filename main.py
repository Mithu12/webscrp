import requests

url = 'https://www.vecteezy.com/free-photos'
req = requests.get(url)

a_string = req.text
indices = [index for index in range(len(a_string)) if a_string.startswith('<img', index)]
total = 0
for i in indices:
    c = i
    tag = ''
    while a_string[c] != '>':
        tag += a_string[c]
        c += 1
    total += 1
    tag += a_string[c]
    print(tag)

print('Total {} tags'.format(total))
