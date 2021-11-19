from selenium import webdriver
import time

# 1.指定url
url = 'http://www.baidu.com'

# 2.创建浏览器对象
driver = webdriver.Chrome()

# 3.访问指定的url地址
driver.get(url)

# driver.get_cookies()可以拿到所有的cookie
print(driver.get_cookies())
print("===="*30)

# 将cookie转化为一个字典
cookies = {}
for data in driver.get_cookies():
    cookies[data['name']] = data['value']
# 上面的三行代码可以使用字典推导式
# cookies = {data['name']:data['value'] for data in driver.get_cookies()}

print(cookies)
time.sleep(20)
driver.quit()
