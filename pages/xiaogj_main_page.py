#coding:utf-8
from time import sleep

from base.base_page import BasePage

class XiaogjMainPage(BasePage):
    '''
    系统登录页及主页
    '''
    '''登录页'''
    login_username = "name"
    login_password = "pwd"
    login_button = "loginBtn"
    '''主页'''
    Enrollment_management_title = 'x, //*[@id="header"]/ul/li[1]/a/span[text()="招生管理"]'
    customerManage_title = 'x, //*[@id="header"]//span[text()="意向客户管理"]'
    username_text = 'x, //*[@id="leftmodules_userinfo"]/div/div[1]/div[1]/span'
    '''退出登录'''
    user_button = 'x, //*[@id="leftmodules_userinfo"]/div/div[1]/div[1]/span'
    logout_button = 'x, //*[@id="leftmodules_userinfo"]/div/div[2]/ul/li[3]/a'

    def login(self, admin_user, admin_password):
        '''
        登录系统
        :param admin_user: 登录用户名
        :param admin_password: 登录密码
        :return: 
        '''
        driver = self.base_driver
        driver.type(self.login_username, admin_user)
        driver.type(self.login_password, admin_password)
        driver.click(self.login_button)
        sleep(2)

    def get_username_text(self):
        '''
        获取登录用户名
        :return: 返回用户名text
        '''
        driver = self.base_driver
        text = driver.get_text(self.username_text)
        return text

    def Go_customerManage(self):
        '''
        进入招生管理模块页面
        :return: 
        '''
        driver = self.base_driver
        driver.move_to_element(self.Enrollment_management_title)
        sleep(1)
        driver.click(self.customerManage_title)
        sleep(1)

    def logout(self):
        '''
        退出系统
        :return: 
        '''
        driver = self.base_driver
        driver.click(self.user_button)
        sleep(1)
        driver.click(self.logout_button)
        sleep(2)