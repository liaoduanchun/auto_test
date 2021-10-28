# coding:utf-8
import csv
import unittest
from time import sleep
from base.box_driver import BoxDriver
from pages.xiaogj_main_page import XiaogjMainPage
from pages.enrollment_management_page import EnrollmentManagementPage

class XiaogjTests(unittest.TestCase):

    def setUp(self):
        url = "https://predemo.xiaogj.com/"
        self.base_driver = BoxDriver("Chrome")
        self.base_driver.maximize_window()
        self.base_driver.implicitly_time(10)
        self.main_page = XiaogjMainPage(self.base_driver)
        self.management_page = EnrollmentManagementPage(self.base_driver)
        self.main_page.open(url)

    def tearDown(self):
        self.base_driver.quit_browser()

    def test_1(self):
        username = 'ldc@predemo2'
        password = 'xiaogj.com'
        username_text = 'x, //*[@id="leftmodules_userinfo"]/div/div[1]/div[1]/span'
        self.main_page.login(username, password)
        sleep(8)
        '''断言'''
        expect_text = 'ldc'
        actual_text = self.base_driver.get_text(username_text)
        self.assertEqual(actual_text, expect_text, msg="与预期结果不符")

        self.main_page.Go_customerManage()
        sleep(5)
        csv_data = self.base_driver.read_csv("F:\\Work\\Auto_test\\data\\customer.csv")
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            customer_data = {
                "name": row[0],
                "sex": row[1],
                "phone": row[2],
                "fathername": row[3],
                "fatherphone": row[4],
                "homeaddres": row[5],
                "zsly": row[6],
                "zzrr": row[7]
            }
            self.management_page.add_customer(customer_data)
            sleep(3)

        csv_data = self.base_driver.read_csv("F:\\Work\\Auto_test\\data\\customer.csv")
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            customer_data = {
                "name": row[0]
            }
            self.management_page.delete_customer(customer_data)
        self.main_page.logout()


if __name__ == "__main__":
    unittest.main()
