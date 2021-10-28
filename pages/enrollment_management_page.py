# coding:utf-8
from time import sleep

from base.base_page import BasePage


class EnrollmentManagementPage(BasePage):
    '''
    意向客户管理
    '''
    '''意向客户管理主页'''
    query_name = 'x, //*[@id="customerManage"]/div/div/div[1]/div[1]/div/input'
    query_button = 'x, //*[@id="customerManage"]/div/div/div[1]/div[6]/div[1]/span/a[1]'
    add_button = 'x, //*[@id="customerManage"]/div/div/div[2]/div[1]/a[1]'
    delete_button = 'x, //*[@id="customerManage"]/div/div/div[2]/div[1]/a[2]'
    select_all_button = 'x, //*[@id="customerManage_table"][2]//thead/tr/th[1]/input[@type="checkbox"]'
    select_button1 = 'x, //*[@id="customerManage_table"]/tbody/tr[1]/td[1]/input[@type="checkbox"]'
    delete_confirm_button = 'x, //*[@id="main_tips-foot"]/button[1]'

    '''新增编辑页面'''
    name_field = 'x, //*[@id="addCustomer"]/div[2]/div[1]/div[1]/div[1]/div/div[1]/input'
    sex_field = 'x, //*[@id="addCustomer"]/div[2]/div[1]/div[1]/div[2]/div/div[1]/select'
    phone_field = 'x, //*[@id="addCustomer"]/div[2]/div[1]/div[1]/div[5]/div/div[1]/input'
    father_name_field = 'x, //*[@id="addCustomer"]/div[2]/div[1]/div[2]/div[1]/div/div[1]/input'
    father_phone_field = 'x, //*[@id="addCustomer"]/div[2]/div[1]/div[2]/div[2]/div/div[1]/input'
    home_address_filed = 'x, //*[@id="addCustomer"]/div[2]/div[1]/div[2]/div[10]/div/div[1]/input'
    zsly_field = 'x, //*[@id="addCustomer"]//input[@placeholder="点击选择招生来源"]'
    zzrr_field = 'x, //*[@id="addCustomer"]//input[@placeholder="点击选择主责任人"]'
    save_button1 = 'x, //*[@id="addCustomer"]/div[4]/button[2]'

    '''选择招生来源窗口'''
    zsly_search_box = 'x, //*[@id="saleModelForm"]//input[@class="model-search-input"]'
    # zsly_search_box = 'x, //*[@id="saleModelFormSingle"]/div[2]/div[1]/div/input'
    zsly_select_button = 'x, //*[@id="saleModelForm"]//div[@class="selectedItem-group"]//label'
    # zsly_select_button = 'x, //*[@id="saleModelFormSingle"]//div[@class="selectedItem-group"]//label/span'
    zsly_confirm_button = 'x, //*[@id="saleModelForm"]//a[text()="确定"]'
    # zsly_confirm_button = 'x, //*[@id="saleModelFormSingle"]//a[text()="确定"]'

    '''选择员工窗口'''
    xzyg_search_box = 'x, //*[@id="empTree_inputsearch"]'
    xzyg_search_title = 'x, //*[@id="empTreeDiv"]/div[1]/div[2]'
    xzyg_confirm_button = 'x, //*[@id="selectEmp_confirm"]'


    def query_customer(self, customer):
        '''
        查询意向客户
        :param customer:需要查询的意向客户 
        :return: 
        '''
        driver = self.base_driver
        driver.type(self.query_name, customer)
        driver.click(self.query_button)
        sleep(1)

    def add_customer(self, customer_data):
        '''
        新增意向客户
        :param customer_data: 新增的意向客户数据
        :return: 
        '''
        driver = self.base_driver
        driver.click(self.add_button)
        sleep(3)
        driver.type(self.name_field, customer_data["name"])
        driver.select_by_visible_text(self.sex_field, customer_data["sex"])
        driver.type(self.phone_field, customer_data["phone"])
        driver.type(self.father_name_field, customer_data["fathername"])
        driver.type(self.father_phone_field, customer_data["fatherphone"])
        driver.type(self.home_address_filed, customer_data["homeaddres"])
        driver.click(self.zsly_field)
        sleep(1)
        driver.type(self.zsly_search_box, customer_data["zsly"])  # 选择招生来源
        driver.click(self.zsly_select_button)
        driver.click(self.zsly_confirm_button)
        driver.click(self.zzrr_field)
        sleep(1)
        driver.type(self.xzyg_search_box, customer_data["zzrr"])  # 选择员工
        sleep(3)
        driver.send_key(self.xzyg_search_box, 'Enter')
        sleep(2)
        driver.click(self.xzyg_confirm_button)
        sleep(1)
        driver.click(self.save_button1)
        sleep(2)

    def delete_customer(self, customer_data):
        '''
        删除意向客户
        :param customer_data: 所需删除的意向客户
        :return: 
        '''
        driver = self.base_driver
        self.query_customer(customer_data["name"])
        sleep(1)
        driver.click(self.select_all_button)
        driver.click(self.delete_button)
        driver.send_key(self.delete_confirm_button, 'Enter')
        sleep(1)
