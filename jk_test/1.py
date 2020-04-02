import requests
import random
import hashlib
import urllib
import json


class BaiduTranslate(object):
    def __init__(self, word):
        self.q = word
        self.fromLang = 'en'
        self.to = 'zh'
        self.appid = '20200402000410670'
        self.salt = random.randint(32768, 65536)
        self.secretKey = 'PPo7isqp6ZDZSnEOr6fT'
        self.sign = self.appid + self.q + str(self.salt) + self.secretKey
        self.baidu_translate = 'http://api.fanyi.baidu.com'
        self.translate_api_url = '/api/trans/vip/translate'
        m1 = hashlib.md5()
        m1.update(self.sign.encode('utf-8'))
        self.sign = m1.hexdigest()
        self.my_url = self.translate_api_url + '?appid=' + self.appid + '&q=' + urllib.request.quote(self.q) + '&from=' + self.fromLang + '&to=' + self.to + '&salt=' + str(self.salt) + '&sign=' + self.sign

    def en_translate_zh(self):
        re = requests.request('post', self.baidu_translate + self.translate_api_url)
        print('\n\t re.text', re.text)
        re_json = json.loads(re.text)
        print('\n\t re_json', re_json)


if __name__ == "__main__":
    bt = BaiduTranslate('test')
    bt.en_translate_zh()
