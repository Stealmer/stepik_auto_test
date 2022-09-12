from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
button = browser.find_element(By.ID, 'book')   
button.click()
x = browser.find_element(By.ID, 'input_value').text

def formula(x):
    return math.log(abs(12 * math.sin(int(x))))

browser.find_element(By.ID, 'answer').send_keys(formula(x))
browser.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()

time.sleep(5)
browser.quit()
