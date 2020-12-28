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
driver.find_element(By.CSS_SELECTOR, 'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > '
                                     'div.nav-collapse.collapse > ul:nth-child(1) > li.dropdown > a').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > '
                                     'div.nav-collapse.collapse > ul:nth-child(1) > '
                                     'li.dropdown.open > ul > li:nth-child(1) > a').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(2) > div > a').click()
sleep(5)
driver.switch_to.frame(driver.find_element_by_class_name(
    'ke-edit-iframe'))
driver.find_element(By.CLASS_NAME, 'ke-content').send_keys('test!test!test!')
driver.switch_to.default_content()
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'body > div.container > div.row > div > form > '
                                     'table > tfoot > tr > td:nth-child(2) > input:nth-child(1)').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, '#form1 > table > tbody > tr > td:nth-child(7) > a:nth-child(2)').click()
driver.switch_to.frame(driver.find_element_by_class_name(
    'ke-edit-iframe'))
driver.find_element(By.CLASS_NAME, 'ke-content').send_keys('test!test!test!')
driver.switch_to.default_content()
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'body > div.container > div.row > div > form > table > '
                                     'tfoot > tr > td:nth-child(2) > input.btn.btn-primary').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, '#tab1 > table > thead > tr > td > span > a:nth-child(4)').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, '#search').send_keys('2020')
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#searchForm > ul > li:nth-child(4) > button').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, '#form1 > table > tbody > tr > td:nth-child(1) > input').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, '#delete').click()
sleep(1)
driver.switch_to.alert.accept()
driver.quit()
