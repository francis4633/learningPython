import time
from selenium import webdriver

# chromedriver解压之后，将chromedriver的目录配置再环境变量中，如果放在chrome
# 浏览器的目录下需要考虑该目录的可读权限，如果没有可读权限代码将无法运行


#通过指定chromedriver的路径来实例化drvier对象,./chromedriver'放在当前目录。
#driver = webdriver.Chrome(executable_path='./chromedriver')

#chromedriver已经添加环境变量
driver = webdriver.Chrome()

#控制浏览器访问url地址
driver.get('https://www.baidu.com/')
time.sleep(3)
#在百度搜索框中搜索‘python’
driver.find_element_by_id('kw').send_keys('python')

#点击‘百度搜索’
driver.find_element_by_id('su').click()

time.sleep(6)

driver.quit()
