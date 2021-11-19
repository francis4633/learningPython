from selenium import webdriver
'''
    无头浏览器的加载
'''
url = 'http://www.baidu.com'

# 创建配置对象
opt = webdriver.ChromeOptions()

# 添加配置参数，设置浏览器为无头模式
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')

# 创建浏览器对象的时候添加配置对象
driver = webdriver.Chrome(chrome_options=opt)

driver.get(url)

# 截屏，并将图片命名为“baidu_到此一游”
driver.save_screenshot('baidu_到此一游.png')
