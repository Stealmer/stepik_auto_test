from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/redirect_accept.html')

driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()

first_window = driver.window_handles[0]
second_window = driver.window_handles[1]
driver._switch_to.window(second_window)

x = driver.find_element(By.ID, 'input_value').text

def formula(x):
    return math.log(abs(12 * math.sin(int(x))))

driver.find_element(By.ID, "answer").send_keys(formula(x))
driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()

time.sleep(5)
driver.quit()
