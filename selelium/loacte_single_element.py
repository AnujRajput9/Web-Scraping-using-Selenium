from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
item = "laptop"
driver.get(f"https://www.flipkart.com/search?q={item}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
elem = driver.find_element(By.CLASS_NAME,"tUxRFH")
# print(elem.get_attribute("outerHTML"))
print(elem.text)

time.sleep(5)
driver.close()