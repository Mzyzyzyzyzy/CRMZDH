from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.implicitly_wait(30)
driver.get('http://192.168.1.211/crm/index.php?m=user&a=login')
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'body > div.container > div > div.span4 > '
                                     'div > form > fieldset > input:nth-child(2)').send_keys('dama')
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'body > div.container > div > div.span4 > '
                                     'div > form > fieldset > input:nth-child(4)').send_keys('admin123456')
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'body > div.container > div > div.span4 > div '
                                     '> form > fieldset > input.btn.btn-primary').click()  # 登录
sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/ul[1]/li[6]/a').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(1) > div > a').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#subject').send_keys('test')
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'body > div.container > div.row > div > form > table > '
                                     'tbody > tr:nth-child(6) > td:nth-child(2) > textarea').send_keys(
    'this is a test !')
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'body > div.container > div.row > div > form > table > '
                                     'tfoot > tr > td:nth-child(2) > input:nth-child(1)').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(7) > '
                                     'a:nth-child(2)').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, '#venue').send_keys('test,test,test!')
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'body > div.container > div.row > div > form > table > '
                                     'tfoot > tr > td:nth-child(2) > input.btn.btn-primary').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, '#search').click()
driver.find_element(By.CSS_SELECTOR, '#search').send_keys('test')
driver.find_element(By.CSS_SELECTOR, '#dosearch').click()
sleep(10)
driver.find_element(By.CSS_SELECTOR, '#form1 > table > tbody > tr > td:nth-child(7) > a:nth-child(3)').click()
driver.quit()
