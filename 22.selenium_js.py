from selenium import webdriver
import time

# 1.指定url
url = 'https://sz.lianjia.com/'

# 2.创建浏览器对象
driver = webdriver.Chrome()

# 3.访问指定url，同时将浏览器的内容全部赋值给driver
driver.get(url)

# 滚动条的拖动
js = 'scrollTo(0,500)'
driver.execute_script(js)


# 如果图片或者其他信息需要滚动后才能加载出来，此时代码会报异常，
# 需在这之前添加一个滚动条的拖动（由于目前该网站已升级，图片已经撤销了）
el_img_button = driver.find_element_by_xpath('')
el_img_button.click()