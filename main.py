import time
from random import randrange
from selenium import webdriver

Timer = 30

ID = input("Enter the ID of the YouTube Video")

link = 'https://youtu.be/' + ID

# print(link)

views = int(input("Enter number of views needed"))

driver = webdriver.Chrome(executable_path="D:\\Projects\\Python\\viewbot\\ENV\\Lib\\chromedriver.exe") #path to the webdriver
driver.get(link)

for i in range(views):
    time.sleep(randrange(Timer))
    driver.refresh()

# driver.quit()
