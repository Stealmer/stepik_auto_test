from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

driver = webdriver.Chrome()
driver.implicitly_wait(15)

#def click(self, xpath):
  #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, xpath)))
    
def create_new_acc():
    driver.find_element(By.ID, 'email_create').send_keys('testRG0002@gmail.com')
    driver.find_element(By.ID, 'SubmitCreate').click()
    gender = driver.find_element(By.ID, 'id_gender1')
    gender.click()
    driver.find_element(By.ID, 'customer_firstname').send_keys('Dmitry')
    driver.find_element(By.ID, 'customer_lastname').send_keys('Afanasyev')
    driver.find_element(By.ID, 'passwd').send_keys('55555')
    driver.find_element(By.ID, 'days').send_keys('22')
    driver.find_element(By.ID, 'months').send_keys('september')
    driver.find_element(By.ID, 'years').send_keys('1989')
    driver.find_element(By.CSS_SELECTOR, 'input[name="address1"]').send_keys('Vorovskogo street, 63a')
    driver.find_element(By.ID, 'city').send_keys('Chelaybinsk')
    driver.find_element(By.CSS_SELECTOR, 'select[name="id_state"]').send_keys('Texas')
    driver.find_element(By.ID, 'postcode').send_keys('00000')
    driver.find_element(By.ID, 'phone_mobile').send_keys('+799999999')
    x = driver.find_element(By.ID, 'alias')
    x.clear()
    x.send_keys('Home')
    driver.find_element(By.ID, 'submitAccount').click()

 
        
def auth_button():        
    driver.find_element(By.CLASS_NAME, 'login').click()
    #time.sleep(2)
    
def logout():
    driver.find_element(By.CLASS_NAME, 'logout').click()
    #time.sleep(2)
    
def sign_in():
    driver.find_element(By.ID, 'email').send_keys('testRG0002@gmail.com')
    driver.find_element(By.ID, 'passwd').send_keys('55555')
    driver.find_element(By.ID, 'SubmitLogin').click()
        

driver.maximize_window()

#[Test]
driver.get('http://automationpractice.com/index.php')
time.sleep(2)
auth_button()
create_new_acc()
time.sleep(2)
logout()
sign_in()

account = driver.find_element(By.LINK_TEXT, 'Dmitry Afanasyev')

if account is None:
    print('Failed')
else:
    print('Passed')
    
driver.quit()