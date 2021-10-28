from time import sleep

from base.box_driver import BoxDriver


class BasePage(object):
    def __init__(self, base_driver: BoxDriver):
        self.base_driver = base_driver

    def open(self, url):
        self.base_driver.navigate(url)
        sleep(2)
