import requests


class RusTxtApi:

    def __init__(self) -> None:
        self.modified_text = ''
        self.percent_unique = 0.0
        self.count_replace = 0
        self.count_symbol = 0
        self.time = 0.0

    def get_nickname(self, count_result=1, len_nick_min=None, len_nick_max=None) -> list:
        if len_nick_min and len_nick_max:
            r = requests.post('https://rustxt.ru/api/index.php',
                              data={'method': 'getNickName', 'count_result': count_result, 'len_nick_min': len_nick_min,
                                    'len_nick_max': len_nick_max})
        else:
            r = requests.post('https://rustxt.ru/api/index.php',
                              data={'method': 'getNickName', 'count_result': count_result})
        if r.status_code == 200:
            return r.json()
        else:
            return None

    def anagram(self, text='') -> dict:
        r = requests.post('https://rustxt.ru/api/index.php', data={'method': 'anagram', 'text': text})
        if r.status_code == 200:
            return r.json()
        else:
            return None

    def get_syn_txt(self, text='') -> str:
        if len(text) >= 5000:
            return 'Много символов! Такое не прокатит'
        r = requests.post('https://rustxt.ru/api/index.php', data={'method': 'getSynText', 'text': text, 'backLight': 1})
        if r.status_code == 200:
            data = r.json()
            self.modified_text = data['modified_text']
            self.percent_unique = data['percent_unique']
            self.count_replace = data['count_replace']
            self.count_symbol = data['count_symbol']
            self.time = data['time']
            return self.modified_text
        else:
            return None

def main():
    api = RusTxtApi()
    print(api.get_nickname(10))

    print(api.time)
    print(api.percent_unique)


if __name__ == '__main__':
    main()
