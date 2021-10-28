#coding:utf-8
import unittest
import time
from base.html_test_runner import HtmlTestRunner
from cases.xiaogj_tests import XiaogjTests


class TestRunner(object):

    def run(self):
        test_suite = unittest.TestSuite()   #实例化测试套件，TestSuite类记得加（）号
        test_suite.addTest(XiaogjTests("test_1"))
        report_path = "F:\\Work\\Auto_test\\reports\\xiaogj_test_report_%s.html" % time.time()
        report_file = open(report_path, mode="wb")

        test_runner = HtmlTestRunner(
            stream = report_file,
            title = u"校管家自动化测试报告",
            description = u"后台测试详情"
        )
        test_runner.run(test_suite)
        report_file.close()