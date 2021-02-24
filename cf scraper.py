from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os 


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://codeforces.com/problemset")
cno = input("Please Enter the contest number ")
#parent_dir= "C:/Users/jishi/OneDrive/Desktop/Desktop data/Eshan/devclub/Web Scraping with Python/"
parent_dir= "./"
oparent_dir=parent_dir
direc=str(cno)
odir=direc 
path = os.path.join(parent_dir, direc) 
opath=path
os.mkdir(path) 
no=cno 
i=0
res = True 
while res :
    cno=str(no)+chr(65+i) 
    try :
        element = driver.find_element_by_link_text(cno)
        res=True 
    except :
        res=False 
    if i==0 :
        while not res :
            search=driver.find_element_by_link_text("→")
            search.click()
            try :
                element = driver.find_element_by_link_text(cno)
                res=True
            except :
                res=False
    if res==False:
        continue 
    parent_dir=opath 
    direc=chr(65+i)
    path = os.path.join(parent_dir, direc) 
    os.mkdir(path)
    element.click() 
    dpath=str(path)+str("/problem.png")
    driver.save_screenshot(dpath)
    inp=driver.find_elements_by_class_name("input") 
    for j in range(len(inp)):
        k=str(j+1)
        name=path+"/input"+k+".txt"
        f=open(name,"x")
        f.write(inp[j].text)
        f.close()
    out=driver.find_elements_by_class_name("output") 
    for j in range(len(out)):
        k=str(j+1)
        name=path+"/output"+k+".txt"
        f=open(name,"x")
        f.write(out[j].text)
        f.close()
    driver.back()
    i=i+1
