import faulthandler

import requests

url = 'https://sam.huat.edu.cn:8443/selfservice/'


response = requests.get(url, verify=faulthandler.disable())
print(response.content)


