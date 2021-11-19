import requests

url = 'http://www.baidu.com'

#response = requests.get(url)

#网上搜索代理IP，免费的有快代理，米朴，在代理网站有只有http，就只能写http,有https，就写https
proxies = {
    'http': 'http://112.192.149.225:47728',
    'https': 'https://112.192.149.225:47728'
}

response = requests.get(url, proxies=proxies)
print(response.text)


