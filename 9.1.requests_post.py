import requests
import json
#import faulthandler

class King(object):
    def __init__(self,word):
        #以下url有问题
        self.url = 'https://ifanyi.iciba.com/index.php?m=fy'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
        }
        self.data = {
            'from': 'en',
            'to': 'auto',
            'q': word
        }
        '''
        self.proxies = {
            'http': 'http://223.241.77.200:3256',
        }
        '''
    def get_data(self):
        response = requests.post(self.url, data=self.data, headers=self.headers)
        return response.content

    def parse_data(self, data):
        #loads方法将json字符串转换成python字典
        dict_data = json.loads(data)

        print(dict_data['content']['out'])

    def run(self):
        #编写爬虫逻辑
        #url
        #headers
        #data字典
        #发送请求获取相应
        response = self.get_data()
        print(response.decode(self, 'utf8'))
        #数据分析
        self.parse_data(response)
if '__main__' == __name__:
    kind = King('字典')
    kind.run()



