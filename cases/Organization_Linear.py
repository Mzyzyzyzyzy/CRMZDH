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
                                     'div.nav-collapse.collapse > ul.nav.pull-right > li:nth-child(6) > a').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR,
                    'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > '
                    'ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(4) > a').click()
driver.find_element(By.CSS_SELECTOR, '#add_department').click()
driver.find_element(By.CSS_SELECTOR, '#name').send_keys('test')
sleep(1)
driver.find_element(By.CSS_SELECTOR,
                    'body > div:nth-child(9) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > '
                    'div > button:nth-child(1) > span').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, '#add_role').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, '#role_add > div:nth-child(1) > div > input').send_keys('software test')
sleep(1)
driver.find_element(By.CSS_SELECTOR,
                    'body > div:nth-child(10) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > '
                    'div > button:nth-child(1) > span').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#user_form > div:nth-child(2) > table > tbody '
                                     '> tr:nth-child(1) > td:nth-child(8) > a:nth-child(2) > i').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(2) > form '
                                     '> table > tbody > tr:nth-child(12) > td:nth-child(2) > input').clear()
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(2) > form '
                                     '> table > tbody > tr:nth-child(12) > td:nth-child(2) > input').send_keys(
    '13111111111')
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(2) > form > table '
                                     '> tfoot > tr > td:nth-child(2) > input.btn.btn-primary').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'body > div.navbar.navbar-inverse.navbar-fixed-top > '
                                     'div > div > a').click()
driver.quit()
