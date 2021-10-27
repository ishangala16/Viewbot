import tkinter as tk
import time
import random
from selenium import webdriver

m = tk.Tk()
m.geometry("300x200")
m.title('View Bot for YouTube')
id_var = tk.StringVar()
views_var = tk.StringVar()


def run():
    id = id_var.get()
    views = views_var.get()
    print("The ID is : " + id)
    print("The no. of views are: " + views)
    id_var.set("")
    views_var.set("")
    Timer = 30

    link = 'https://www.youtube.com/watch?v=' + id

    # print(link)

    driver = webdriver.Chrome("D:\\Projects\\Python\\viewbot\\ENV\\Lib\\chromedriver.exe")
    driver.get(link)

    for i in range(views):
        time.sleep(random.randrange(Timer))
        driver.refresh()


L1 = tk.Label(m, text="id", font=('bold')).grid(row=0)
L2 = tk.Label(m, text="views", font=('bold')).grid(row=1)

E1 = tk.Entry(m, textvariable=id_var, bd=5).grid(row=0, column=1)
E2 = tk.Entry(m, textvariable=views_var, bd=5).grid(row=1, column=1)

button = tk.Button(m, text="Run", width=25, command=run).grid(row=3)

m.mainloop()
