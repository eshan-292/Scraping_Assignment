from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")
search = driver.find_element_by_id("username") 
search.clear()
username=input("Enter Your Username ")
password=input("Enter Your Password ")
search.send_keys(username)
search = driver.find_element_by_id("password") 
search.clear()
search.send_keys(password)
text = driver.find_element_by_id("login").text
a=text.find("add")
s=text.find("subtract")
f=text.find("first")
e=text.find("second")
if a!=-1 :
    res = [int(i) for i in text.split() if i.isdigit()]
    ans=res[0]+res[1] 
elif s!=-1:
    res = [int(i) for i in text.split() if i.isdigit()]
    ans=res[0]-res[1] 
elif f!=-1 :
    res = [int(i) for i in text.split() if i.isdigit()]
    ans=res[0] 
elif e!=-1 :
    res = [int(i) for i in text.split() if i.isdigit()]
    ans=res[1] 

search = driver.find_element_by_id("valuepkg3") 
search.clear()
search.send_keys(ans)
search.send_keys(Keys.RETURN)