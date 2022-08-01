class Util:
    search_tags = []
    response_str = ''
    count = 0

    def __init__(self, text, tags):
        self.response_str = text
        self.search_tags = tags

    def get_atr_data(self, data_type, c):
        result = ''

        if self.response_str.startswith(data_type, c):
            # skipping 'src="','alt="' characters
            result_start = c + 5
            while self.response_str[result_start] != '"':
                result = result + self.response_str[result_start]
                result_start += 1
        if result != '':
            return result
        else:
            return ''

    def filter_by_tags(self, src, alt):
        for tag in self.search_tags:
            if src.find(tag) != -1 or alt.find(tag) != -1:
                print(src)
                return 1
        return 0

    def filter_images(self, c):
        src = ''
        alt = ''
        while self.response_str[c] != '>':
            if src == '':
                src = self.get_atr_data('src=', c)
            if alt == '':
                alt = self.get_atr_data('alt=', c)
            c += 1

        self.count += self.filter_by_tags(src.lower(), alt.lower())
