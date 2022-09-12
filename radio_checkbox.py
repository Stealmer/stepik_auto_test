from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/math.html")

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

browser.find_element(By.ID, "answer").send_keys(y)
browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()