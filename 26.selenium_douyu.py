from selenium import webdriver
import time

class Douyu(object):

    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()



    def parse_date(self):
        room_list = self.driver.find_elements_by_xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li/div')
        print("第一页的直播有 {} 条".format(len(room_list)))

        data_list = []

        # 遍历房间列表，从每一个房间节点中获取数据
        for room in room_list:
            temp = {}

            temp['title'] = room.find_element_by_xpath('./a[1]/div[2]/div[1]/h3').text
            temp['type'] = room.find_element_by_xpath('./a[1]/div[2]/div[1]/span').text
            temp['owner'] = room.find_element_by_xpath('./a[1]/div[2]/div[2]/h2').text
            temp['num'] = room.find_element_by_xpath('./a[1]/div[2]/div[2]/span').text
            temp['img'] = room.find_element_by_xpath('./a[1]/div[1]/div[1]/picture/img').get_attribute('src')
            # print(temp)
            data_list.append(temp)
        return data_list

    def save_data(self,data_list):
        for data in data_list:
            print(data)

    def run(self):
        # url
        # driver
        # get
        self.driver.get(self.url)

        while True:

            # parse
            data_list = self.parse_date()
            # save
            self.save_data(data_list)
            # next
            try:
                #由于现在斗鱼直播网有问题，无法正常访问，此处展示不行
                el_next = self.driver.find_element_by_xpath('//*[contains(text(),"下一页")]')
                self.driver.execute_script('scrollTo(0,100000)')
                print(el_next)
                el_next.click()

            except:
                break


        time.sleep(60)
        self.driver.quit()

if __name__ == '__main__':
    douyu = Douyu()
    douyu.run()
