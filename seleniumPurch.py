from selenium import webdriver
import time
timeToBuy = "2:12"

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://miacomet.ezlinksgolf.com/index.html#/search")
time.sleep(5)
x = driver.find_elements_by_tag_name(timeToBuy)
y = 0
for i in x:
    if timeToBuy in i.text:
        print ("success")
        print(i.text)
    else:
        print("fail")
    

    y +=1
print(y)
