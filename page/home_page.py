
from selenium.webdriver.common.by import By    #引入By类
from page.base_page import BasePage        #调用类

class Homepage():      #定义一个类
    _url=BasePage._url+"/crm/index.php?m=dynamic&a=index"     #设置url地址
    def __init__(self,driver,url=None):     #将类实例化
        self.driver=driver
        if not url:
            self.url=self._url
    username_locator=(By.CSS_SELECTOR,"body > div.navbar.navbar-"
                "inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse >"
                " ul:nth-child(1) > li:nth-child(1) > a")   #找寻一个目标，用于后面记那些具体操作

    def get_username_text(self):    #定义一个类
        return self.driver.find_element(*self.username_locator).text  #返回找到目标的文本
# -*- coding: utf-8 -*-
# @Time : 2020/12/26 22:41
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : home_page.py
# @Project : CrmZDH.test
from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类
from time import sleep  # 引入时间
class loginpage(BasePage):
    # 重写url属性，父类的url+/crm拼接
    _url = BasePage._url + "/admin"
    # 页面属性
    # 用户名输入框定位器
    username_locator = (By.NAME, "username")
    # 密码输入框定位器
    password_locator = (By.NAME, "password")
    # 登录按钮定位器
    submit_locator = (By.CSS_SELECTOR,"input[value='进入管理中心']")

    def input_uesrname(self, username):  # 定义一个类，用于找到用户名输入框并进行输入
        element = self.find_element(self.username_locator)
        element.clear()
        element.send_keys(username)
        sleep(2)  # 暂时2秒

    def input_password(self, password):  # 定义一个类，用于找到密码输入框并进行输入
        element = self.find_element(self.password_locator)
        element.clear()
        element.send_keys(password)
        sleep(3)

    def sumbit(self):  # 定义一个类，用于找到按钮并点击
        self.find_element(self.submit_locator).click()
        sleep(3)

    def login(self, username, passwrod):  # 定义一个函数集合，用于进行登录的一些操作
        self.open()
        self.input_uesrname(username)
        self.input_password(passwrod)
        self.sumbit()

