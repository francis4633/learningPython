from selenium import webdriver
import time

url = 'http://www.baidu.com'

# 创建一个浏览器对象
driver = webdriver.Chrome()

# 访问指定的url地址，将所有信息保存在driver中
driver.get(url)

# 显示源码(driver.page_source:获取当前标签页浏览器渲染之后的网页源代码)
# print(driver.page_source)
# # 显示响应之后对应的url,请求的url是http,响应之后编程了https
# print(driver.current_url)
#
# time.sleep(2)
# driver.get('http://www.douban.com')
# time.sleep(2)
# # 返回至百度
# driver.back()
#
# #这些休眠时加载之后的2秒
# time.sleep(2)
# # 前进，再次进入豆瓣
# driver.forward()
#
# time.sleep(2)
# # 关闭当前的标签页，当前标签页是在豆瓣，如果只有一个豆瓣标签，则在关闭标签页之后同时关闭浏览器
# driver.close()


# 页面截图，保存在当前目录 作用：常用于安正是否运行或者验证码截图。
# 登陆注册时有些时有些是图片验证码，且每次请求都变化的，需要通过保存这张截图来分析图片中的验证码 www.yundama.com中的验证码便是如此
driver.save_screenshot('baidu.png')
# 关闭浏览器
# driver.quit()

