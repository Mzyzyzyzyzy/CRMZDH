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
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > '
                                     'div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(2) > a').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'body > div.container > div.row > '
                                     'div:nth-child(1) > div > a').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#name').send_keys('Test8')
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#form1 > table > tfoot > tr > td > input:nth-child(1)').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > '
                                     'td:nth-child(12) > a:nth-child(2)').click()
sleep(3)
driver.find_element(By.CSS_SELECTOR, '#description').send_keys('this is a test! over over !')
sleep(3)
driver.find_element(By.CSS_SELECTOR, '#form1 > table > tfoot > tr > td > input.btn.btn-primary').click()
sleep(5)
driver.find_element(By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > '
                                     'td:nth-child(3) > a > span').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#tab1 > div.container2.top-pad > div > '
                                     'a.btn.btn-primary.del_confirm').click()
sleep(1)
driver.switch_to.alert.accept()
driver.find_element(By.CSS_SELECTOR, 'body > div.navbar.navbar-inverse.navbar-fixed-top '
                                     '> div > div > a').click()
sleep(2)
driver.quit()
