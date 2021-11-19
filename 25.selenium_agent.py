from selenium import webdriver
import time

'''
    selenium代理:访问会慢一点
'''
url = 'http://www.baidu.com'

# 创建配置对象
opt = webdriver.ChromeOptions()

# 添加配置参数，更换IP代码必须重新启动浏览器
# opt.add_argument('–proxy-server=http://8.218.81.68:59394')
# 更换user-agent
opt.add_argument('-user-agent=Mozilla/5.0 python39')

# 创建浏览器对象的时候添加配置对象
driver = webdriver.Chrome(chrome_options=opt)
#driver = webdriver.Chrome()
driver.get(url)

time.sleep(20)
driver.quit()


