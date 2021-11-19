from selenium import webdriver
import time

url = 'https://sz.58.com/'

# 创建一个浏览器对象
driver = webdriver.Chrome()

# 访问指定的url地址，并将所有的信息保存在driver中
driver.get(url)

# 事先打印以下当前的url和window_handles
print('点击之前的url地址为：{}'.format(driver.current_url))
print('点击之前的window_handles为：{}'.format(driver.window_handles))

# 定位并点击租房按钮
el = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[3]/a')
el.click()

# 打印点击之后的url和window_handles
print('点击之后的url地址为：{}'.format(driver.current_url))
print('点击之后的window_handles为：{}'.format(driver.window_handles))

# 通过前后两个打印对比发现，两者是一样的，所以即使点击了，句柄也在点击之前的目录上，需要通过以下进行句柄的转移
driver.switch_to.window(driver.window_handles[-1])
el_list = driver.find_elements_by_xpath('/html/body/div[6]/div[2]/ul/li/div[2]/h2/a')
print(len(el_list))
print('点击之后的url地址为：{}'.format(driver.current_url))
print('点击之后的window_handles为：{}'.format(driver.window_handles))

time.sleep(20)
driver.quit()

