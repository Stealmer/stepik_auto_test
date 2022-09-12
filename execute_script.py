from cmath import sin
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def formula(x):
    return math.log(abs(12 * sin(int(x))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element(By.ID, 'input_value').text
y = formula(x)
browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]').send_keys(y)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
browser.find_element(By.ID, 'robotCheckbox').click()
browser.find_element(By.ID, 'robotsRule').click()
button.click()
time.sleep(5)
browser.quit()