import requests
import jsonpath
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}

response = requests.get('https://www.lagou.com/lbs/getAllCitySearchLabels.json',headers=headers)

dict_data = json.loads(response.content)
#获取A下所有的name
#print(jsonpath.jsonpath(dict_data, '$..A..name'))
#获取所有的城市名
print(jsonpath.jsonpath(dict_data, '$..name'))
