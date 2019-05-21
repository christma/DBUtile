import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Exec.dbutil.DB_connetion_pool import getPTConnection


def main():
    chrome_options = Options()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver1 = webdriver.Chrome(executable_path='D:\chromedirver\chromedriver.exe', chrome_options=chrome_options)
    driver1.get("https://cloud.tmall.com/console/newRdsDetail.htm?resId=76010")
    time.sleep(5)
    driver1.get("https://console.cloud.tmall.com/?spm=0.12349310.0.0.44f81e9b8qHTMr#/aliyun/product?productCode=ecs")
    driver1.implicitly_wait(20)
    elements = driver1.find_elements_by_xpath('//tr[@class="ng-scope"]')
    print(len(elements))
    i = 0
    while (len(elements) == 20):
        list = []
        time.sleep(10)
        elements = driver1.find_elements_by_xpath('//tr[@class="ng-scope"]')
        for element in elements:
            datas = {}
            datas['instanceID'] = element.find_element_by_xpath('./td[@class="rds-list-instance-name-td"]/div/div/a[1]').text
            datas['instance_type'] = element.find_element_by_xpath('./td[5]/span').text
            datas['db_type'] = element.find_element_by_xpath('./td[6]/span').text
            times = element.find_element_by_xpath('./td[8]/span').get_attribute("time")
            if times:
                times = times.split("T")[0]
            datas['end_time'] = times
            datas['description'] = element.find_element_by_xpath('./td[2]/DIV/DIV/span').get_attribute("c-text")
            list.append(datas)

        # with getPTConnection() as db:
        #     try:
        #         for data in list:
        #             sql2 = "REPLACE INTO dbabase_rdsmessage(dbInstanceName,description,dbInstanceClass,engine,endTime) VALUES ('{}','{}','{}','{}','{}'); " \
        #                 .format(data['instanceID'], data['description'], data['instance_type'], data['db_type'], data['end_time'])
        #             print(sql2)
        #             db.cursor.execute(sql2)
        #         db.conn.commit()
        #     except Exception as e:
        #         print(e)
        #         pass
        print(len(elements))
        i += 1
        print('第 ', i, ' 页')
        driver1.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/table[2]/tfoot/tr/td[2]/div[2]/div/ul/li[6]/a").click()
    driver1.close()



if __name__ == '__main__':
    main()