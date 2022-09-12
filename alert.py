from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import math
import time

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/alert_accept.html')

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
confirm = driver.switch_to.alert
confirm.accept()

x = driver.find_element(By.ID, 'input_value').text

def formula(x):
    return math.log(abs(12 * math.sin(int(x))))

driver.find_element(By.ID, 'answer').send_keys(formula(x))
driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()

time.sleep(5)
driver.quit()
