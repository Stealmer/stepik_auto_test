from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import math

def calc(treasure_x):
  return str(math.log(abs(12*math.sin(int(treasure_x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/get_attribute.html")

treasure = browser.find_element(By.ID, "treasure")
treasure_x = treasure.get_attribute("valuex")
y = calc(treasure_x)

browser.find_element(By.ID, "answer").send_keys(y)
browser.find_element(By.ID, "robotCheckbox").click()
browser.find_element(By.ID, "robotsRule").click()
browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(5)
browser.quit()


