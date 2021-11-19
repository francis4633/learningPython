from selenium import webdriver

# 1.指定url
url = 'http://www.baidu.com'

# 2.创建浏览器对象
driver = webdriver.Chrome()

# 隐式等待：设置位置之后的所有元素定位操作都有最大等待时间10秒，在10秒内会定期进行元素的定位，
# 操作设置时间之后将会报错
driver.implicitly_wait(10)

# 3.访问指定的url地址
driver.get(url)

# 获取百度的那张图片
el = driver.find_element_by_xpath('//*[@id="s_lg_img"]')
print(el)
