# -*- coding: utf-8 -*-
from atf import *
from atf.ui import *
from atf.ui.should_be import Enabled
from selenium.webdriver.common.by import By


class MainPage(Region):
    """Главная страница сайта"""
    conf_lnk = Element(By.CLASS_NAME, 'NavigationPanels-NavSchemeLink__link-hover')
    company_lnk = Element(By.XPATH, './/*[@name="tileContainer"]/div[11]')

    def change_conf(self):
        self.conf_lnk.click()
        self.company_lnk.click()
