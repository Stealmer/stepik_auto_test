from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/file_input.html')

first_name = driver.find_element(By.CSS_SELECTOR, "input[name = 'firstname']").send_keys('Dmitry')
second_name = driver.find_element(By.CSS_SELECTOR, "input[name = 'lastname']").send_keys('Afanasyev')
email = driver.find_element(By.CSS_SELECTOR, "input[name = 'email']").send_keys('stealmer@gmail.com')

element = driver.find_element(By.ID, "file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'bio.txt')
element.send_keys(file_path)
submit = driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']")
submit.click()
time.sleep(5)
driver.quit()
