import requests

url  = "https://www.baidu.com/s?wd=python"

#构建请求头字典
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}

response = requests.get(url, headers=headers)

#将文件写入到baidu.html文件中，并生成一个baidu.html文件
with open("baidu.html", 'wb')as f:
    f.write(response.content)