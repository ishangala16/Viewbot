import time  # this module provides time related functions
from selenium import webdriver  # this module provides all web driver implementations
import random  # random choice generation

Timer = 30  # time for page to refresh
ID = input("Enter the Quora Link: ")  # input link to be view botted
views = int(input("Enter number of views needed: "))  # input views

from proxyscrape import create_collector  # this module retrieves free proxies

collector = create_collector('my-collector', 'https')  # create a collector for https resources
collector.apply_filter({'type': 'https', 'anonymous': True})  # filtering out proxies

for i in range(views):
    proxy = collector.get_proxy()  # Retrieve https proxy

    proxy1 = proxy.host + ":" + proxy.port

    PROXY = proxy1  # use working proxies

    chrome_options = webdriver.ChromeOptions()  # Using Chrome options to add proxy attribute
    chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

    driver = webdriver.Chrome(executable_path="D:\\Projects\\Python\\viewbot\\ENV\\Lib\\chromedriver.exe",
                              chrome_options=chrome_options)  # Change the executable path according to where the
    # driver is located
    try:
        driver.get(ID)  # fetch url
        print("Proxy Success")
    except:  # Code to handle exceptions (In this case proxy failure)
        print("Proxy Error")
        driver.close()
        continue
    time.sleep(random.randrange(Timer))  # Generate random amount of time to be spent on a page.
    driver.close()  # Exits the driver

# Enjoy View botting!!