from selenium import webdriver
import time

url = 'http://www.baidu.com'

# 创建一个浏览器对象
driver = webdriver.Chrome()

# 访问指定的url地址，将所有信息保存在driver中
driver.get(url)

# 通过xpath进行元素定位,已被弃用
el_list = driver.find_elements_by_xpath('/html/body/div[6]/div[2]/ul/li/div[2]/h2/a')
for el in el_list:
    print(el)
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python3')
# 通过css选择器进行元素定位
# driver.find_element_by_css_selector('#kw').send_keys('python3')
# 通过lname属性值进行元素定位
# driver.find_element_by_name('wd').send_keys('python3')

# 通过class属性值进行元素定位
# driver.find_element_by_class_name('s_ipt').send_keys('python3')

# driver.find_element_by_id('su').click()

# 通过链接文本进行元素定位(定位之后直接click):但如果文本不精确会定位不到，报异常,此时可以采用find_element_by_partial_link_text
# driver.find_element_by_link_text('hao123').click()
# driver.find_element_by_partial_link_text('hao').click()
# 目标元素在当前html中是唯一标签的时候或者是众多定位出来的标签中的第一个的时候才能使用
#print(driver.find_element_by_tag_name('title'))


#time.sleep(20)
#driver.quit()

# find_element_by_xxx
#     定位到则是一个对象
#     定位不到则包异常
# find_elements_by_xxx
#     定位到则是一个含有元素的列表
#     定位不到则是一个空列表
