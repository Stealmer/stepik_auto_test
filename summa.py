from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
 
    
driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/selects1.html')

x = driver.find_element(By.ID, 'num1').text
y = driver.find_element(By.ID, 'num2').text

z = int(x) + int(y)
driver.find_element(By.ID, 'dropdown').click()
sel = Select(driver.find_element(By.TAG_NAME, 'select'))
sel.select_by_visible_text(str(z))
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
driver.quit()