import requests
import re #导入正则模块
'''
    任务：使用requests.session来完成github登陆，并获取需要登陆后才能访问的页面
   1、本示例的主要关键点是在 url2登陆这里，该请求时post请求，需要分析其每一个参数从何而来
   2、本文中的cookies放在了session中保存
'''
def login():
    # session
    session = requests.session()

    # headers
    session.headers = {

        #'user-agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/94.0.4606.71Safari / 537.36'
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }

    # 1、url1 -- 获取token、timetamps、timetampsSecret
    url1 = 'https://github.com/login'
    # 1.1、发送请求获取相应
    res_1 = session.get(url1).content.decode()
    # 1.2、正则提取(value加上括号则会获取括号内的内容，value括号内的点代表匹配所有，*代表多个)
    token = re.findall('name="authenticity_token" value="(.*?)" />', res_1)[0]
    timetamps = re.findall('<input type="hidden" name="timestamp" value="(.*?)"', res_1)[0]
    timetampsSecret = re.findall('<input type="hidden" name="timestamp_secret" value="(.*?)"', res_1)[0]
    # 打印是否获取到了value的值
    # print(token)
    # print(timetamps)
    # print(timetampsSecret)

    # 2、url2 -- 登陆
    url2 = 'https://github.com/session'
    # 2.1、构建表单数据
    data = {
        'commit': 'Sign in',
        'authenticity_token': token,
        'login': '674145395@qq.com',
        'password': 'ffy27@live.cn',
        'trusted_device': '',
        'webauthn-support': 'supported',
        'webauthn-iuvpaa-support': 'unsupported',
        'return_to': url1,
        'allow_signup': '',
        'client_id': '',
        'integration': '',
        'required_field_1f20': '',
        'timestamp': timetamps,
        'timestamp_secret': timetampsSecret
    }
    # 2.2、发送请求登陆
    session.post(url2, data=data)
    #3、url3 -- 验证
    url3 = 'https://github.com/francis4633'
    response = session.get(url3)

    with open('github_SignIn.html', 'wb')as f:
        f.write(response.content)

if '__main__' == __name__:
    login()
