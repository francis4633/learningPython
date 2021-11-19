from selenium import webdriver
import time

# 1、定义一个url
url = 'https://qzone.qq.com/'

# 2、创建一个浏览器对象
driver = webdriver.Chrome()

# 3、访问指定的url地址，同时将url的信息全部放入到driver中
driver.get(url)
# frame中直接用id，由于二维码是在iframe中，iframe中的元素不能直接访问，需要定位到iframezhong
# driver.switch_to.frame('login_frame')
# 有时候id生成的，不靠谱，可以采用xpath,修改id,例如163邮箱登陆的登陆iframe:https://mail.163.com/
el_frame = driver.find_element_by_xpath('//*[@id="login_frame"]')
driver.switch_to.frame(el_frame)

driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('674145395')
driver.find_element_by_id('p').send_keys('ffy72@live.cn')
driver.find_element_by_id('login_button').click()


time.sleep(20)
driver.quit()

