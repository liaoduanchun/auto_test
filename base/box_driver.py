# coding:utf-8
import csv
from time import sleep
import openpyxl as xl
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import xlrd

class BoxDriver(object):
    '''定义driver构造函数'''

    def __init__(self, a):
        '''
        选择浏览器
        :param a:选择浏览器 
        '''
        if a == "Chrome":
            driver = webdriver.Chrome()
            try:
                self.driver = driver
            except Exception:
                raise NameError("Chrome Not Found")
        elif a == "Firefox":
            driver = webdriver.Firefox()
            try:
                self.driver = driver
            except Exception:
                raise NameError("Firefox Not Found")
        else:
            raise NameError("Not Found Any Browser")

    def get_element(self, selector):
        '''
        元素定位
        :param selector: 元素定位，例：'i, name'
        :return: 
        '''
        if ',' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split(',')[0]  # 定位方式
        selector_value = selector.split(',')[1]  # 定位的值

        if selector_by == "id" or selector_by == "i":
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == "name" or selector_by == "n":
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "css" or selector_by == "c":
            element = self.driver.find_element_by_css_selector(selector_value)
        elif selector_by == "xpath" or selector_by == "x":
            element = self.driver.find_element_by_xpath(selector_value)
        elif selector_by == "class_name" or selector_by == "cn":
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "link_text" or selector_by == "lt":
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "tag_name" or selector_by == "tn":
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "partial_link_name" or selector_by == "pln":
            element = self.driver.find_element_by_partial_link_text(selector_value)
        else:
            raise NameError("please enter a valid type of targeting element")
        return element

    def type(self, selector, text):
        '''
        向输入框输入内容
        :param selector: 输入框元素定位
        :param text: 所需输入的内容
        :return: 
        '''
        ele = self.get_element(selector)
        ele.clear()
        ele.send_keys(text)

    def click(self, selector):
        '''
        鼠标左键单击
        :param selector: 
        :return: 
        '''
        ele = self.get_element(selector)
        ele.click()

    def switch_to_frame(self, selector):
        '''
        进入iframe
        :param selector: iframe元素
        :return: 
        '''
        ele = self.get_element(selector)
        self.driver.switch_to.frame(ele)

    def switch_default_frame(self):
        '''
        退出iframe
        :return: 
        '''
        self.driver.switch_to.default_content()

    def select_by_index(self, selector, index):
        '''
        以index方式选择select下拉框选项
        :param selector: 下拉框元素定位
        :param index: 下拉框选项值（index）
        :return: 
        '''
        ele = self.get_element(selector)
        select = Select(ele)
        select.select_by_index(index)

    def select_by_value(self, selector, value):
        '''
        以value方式选择select下拉框选项
        :param selector: 下拉框元素定位
        :param value: 下拉框选项值（value）
        :return: 
        '''
        ele = self.get_element(selector)
        select = Select(ele)
        select.select_by_value(value)

    def select_by_visible_text(self, selector, text):
        '''
        以text方式选择select下拉框选项
        :param selector: 下拉框元素定位
        :param text: 下拉框选项值（text）
        :return: 
        '''
        ele = self.get_element(selector)
        select = Select(ele)
        select.select_by_visible_text(text)

    def quit_browser(self):
        '''
        退出浏览器
        :return: 
        '''
        sleep(2)
        self.driver.quit()

    def close_browser(self):
        '''
        关闭浏览器
        :return: 
        '''
        self.driver.close()

    def maximize_window(self):
        '''
        窗口最大化
        :return: 
        '''
        self.driver.maximize_window()

    def navigate(self, url):
        '''
        打开url
        :param url: url地址
        :return: 
        '''
        self.driver.get(url)

    def implicitly_time(self, time):
        '''
        设置等待时间
        :param time: 时间参数
        :return: 
        '''
        self.driver.implicitly_wait(time)

    def get_title(self):
        '''
        获取当前标题
        :return: 
        '''
        return self.driver.title

    def refresh_browser(self):
        '''
        刷新当前页面
        :return: 
        '''
        self.driver.refresh()

    def get_url(self):
        '''
        获取当前页面URL
        :return: 
        '''
        ele = self.driver.current_url
        return ele

    def get_text(self, selector):
        '''
        获取元素文本
        :param selector: 元素定位
        :return: 
        '''
        ele = self.get_element(selector).get_attribute('innerText')
        return ele

    def alert(self, x):
        '''
        确认/取消对话框
        :param x: Y or N
        :return: 
        '''
        if x == "accept" or x == "Y":
            self.driver.switch_to.alert().accept()
        elif x == "dismiss" or x == "N":
            self.driver.switch_to.alert().dismiss()

    def date(self, selector, date):
        '''
        日期选择框
        :param selector: 日期选择框元素定位
        :param date: 所需选择的日期（2020-01-01）
        :return: 
        '''
        ele = self.get_element(selector)
        ele.clear()
        ele.send_keys(date)
        ele.send_keys(Keys.ENTER)

    def select_input(self, selector, value):
        '''
        下拉输入选择框
        :param selector: 下拉输入框元素定位
        :param value: 需要选择的值
        :return: 
        '''
        ele = self.get_element(selector)
        ele.click()
        ele.send_keys(value)
        ele.send_keys(Keys.ENTER)

    def read_csv(self, csv_file):
        '''
        读取CSV文件数据
        :param csv_file: csx文件路径
        :return: 
        '''
        self.csv_file = open(csv_file, mode="r", encoding="UTF-8")
        csv_data = csv.reader(self.csv_file)
        return csv_data

    def improt_accessory(self, selector, file):
        '''
        附件导入
        :param selector: 元素点位
        :param file: 附件导入路径
        :return: 
        '''
        ele = self.get_element(selector)
        ele.send_keys(file)

    def select2(self, selector1, selector2, n):
        '''
        2元素单选框
        :param selector1: 元素1
        :param selector2: 元素2
        :param n: 需要选择的元素序号
        :return: 
        '''
        if n == "1" or n == "男":
            self.click(selector1)
        elif n == "2" or n == "女":
            self.click(selector2)

    def checkbox(self, list):
        '''
        复选框选择
        :param list: 元素定位list
        :return: 
        '''
        for i in list:
            ele = self.get_element(i)
            ele.click()

    def list_change(self, str):
        '''
        列表转化
        :param str: 字符串,例：'["Google"|"Runoob"|"Taobao"|"Facebook"]'
        :return: list
        '''
        list = []
        if str:
            str1 = str.split('[')[1]  #截取 [ 符号右半部分
            str2 = str1.split(']')[0]  #截取 ] 符号左半部分
            str3 = str2.split('|')  #以 | 符号分割
            for i in str3:
                a = i.lstrip('\"')
                b = a.rstrip('\"')
                list.append(b)
        return list

    def switch_window(self):
        '''
        切换窗口
        :return: 
        '''
        nowwindow = self.driver.current_window_handle #获取当前窗口句柄
        windows = self.driver.window_handles #获取当前所有窗口句柄
        for window in windows:
            if window != nowwindow:
                self.driver.switch_to.window(window)

    def get_attribute(self, selector, attribute):
        '''
        获取元素属性值
        :param selector: 元素定位
        :param attribute: 元素属性
        :return: 
        '''
        ele = self.get_element(selector)
        return ele.get_attribute(attribute)

    def move_to_element(self, selector):
        '''
        模拟鼠标移动
        :param selector: 元素定位
        :return: 
        '''
        ele = self.get_element(selector)
        webdriver.ActionChains(self.driver).move_to_element(ele).perform()

    def list_dict(self, list1, list2):
        '''
        将两个列表合并成一个字典
        :param list1:key
        :param list2:value
        :return:dict
        '''
        dic = dict(map(lambda x, y: [x, y], list1, list2))
        return dic

    def excel_to_list(self, data_file, sheet):
        '''
        将execl数据转化为list
        :param data_file: execl表格文件路径
        :param sheet: execl表格 工作簿
        :return: list
        '''
        data_list = []  # 新建个空列表，来乘装所有的数据
        wb = xlrd.open_workbook(data_file)  # 打开excel
        sh = wb.sheet_by_name(sheet)  # 获取工作簿
        header = sh.row_values(0)  # 获取标题行数据
        for i in range(1, sh.nrows):  # 跳过标题行，从第二行开始取数据
            d = dict(zip(header, sh.row_values(i)))  # 将标题和每行数据组装成字典
            data_list.append(d)
        return data_list  # 列表嵌套字典格式，每个元素是一个字典

    def get_test_data(self, data_list, case_name):
        for case_data in data_list:
            if case_name == case_data['case_name']:  # 如果字典数据中case_name与参数一致
                return case_data

    def send_key(self, selector, key):
        '''
        模拟键盘操作
        :param key: 
        :return: 
        '''
        if key == 'Enter':
             k = self.get_element(selector).send_keys(Keys.ENTER)
        elif key == 'Backspace':
             k = self.get_element(selector).send_keys(Keys.BACKSPACE)
        elif key == 'Space':
             k = self.get_element(selector).send_keys(Keys.SPACE)
        elif key == 'Delete':
             k = self.get_element(selector).send_keys(Keys.DELETE)
        else:
            raise NameError("please enter a valid value of operation keyboard")
        return k


