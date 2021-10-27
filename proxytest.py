import requests

from selenium import webdriver
from rotatingproxy import proxy1
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# url = 'https://httpbin.org/ip'
# response = requests.get(url, proxies=proxies)
proxies = {
    # "https": 'https://183.162.159.84:4216',
    # "https": 'http://209.50.52.162:9050'
}
# print(response.json())
# driver = webdriver.Chrome(executable_path="D:\\Projects\\Python\\viewbot\\ENV\\Lib\\chromedriver.exe")


PROXY =proxy1


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
try:
    driver = webdriver.Chrome(executable_path="D:\\Projects\\Python\\viewbot\\ENV\\Lib\\chromedriver.exe", chrome_options=chrome_options)
    # driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":""})
    driver.get('http://httpbin.org/ip')
    # driver.quit()
except:
    print("Proxy does not work")

