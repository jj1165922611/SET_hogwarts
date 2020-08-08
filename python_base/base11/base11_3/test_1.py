from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.layui.com/demo/upload.html")
sleep(2)
ele=driver.find_element(By.ID,"test1")
driver.execute_script("arguments[0].click();",ele)

sleep(20)
driver.quit()