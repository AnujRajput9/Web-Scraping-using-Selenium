from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
item = "laptop"
for i in range(1,10):
    driver.get(f"https://www.flipkart.com/search?q={item}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")
    elems = driver.find_elements(By.CLASS_NAME,"tUxRFH")
    print("no of elements ",len(elems))
    for elem in elems:
        print(elem.text)
    time.sleep(5)
    driver.close()