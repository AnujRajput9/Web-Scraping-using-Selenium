from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
item = "laptop"
itemNo =0
for i in range(1,15):
    driver.get(f"https://www.flipkart.com/search?q={item}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")
    elems = driver.find_elements(By.CLASS_NAME,"tUxRFH")
    print("no of elements ",len(elems))
    for elem in elems:
        d=elem.get_attribute("outerHTML")
        with open(f"data/{item}_{itemNo}.html",'w',encoding="utf-8") as f:
            f.write(d)
            itemNo  += 1
    time.sleep(1)
driver.close()