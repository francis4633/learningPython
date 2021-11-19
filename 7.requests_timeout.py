import requests

url = "https://twitter.com"
#3s超时
response = requests.get(url, timeout=3)


