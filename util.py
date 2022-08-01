def get_atr_data(response_str, data_type, c):
    result = ''
    if response_str.startswith(data_type, c):
        # skipping 'src="','alt="' characters
        result_start = c + 5
        while response_str[result_start] != '"':
            result = result + response_str[result_start]
            result_start += 1
    if result != '':
        return result
    else:
        return ''


def filter_images(response_str, c):
    src = ''
    alt = ''
    while response_str[c] != '>':
        if src == '':
            src = get_atr_data(response_str, 'src=', c)
        if alt == '':
            alt = get_atr_data(response_str, 'alt=', c)
        c += 1
    print(src)
