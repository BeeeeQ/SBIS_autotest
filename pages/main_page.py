# -*- coding: utf-8 -*-
from atf import *
from atf.ui import *
from atf.ui.should_be import Enabled
from selenium.webdriver.common.by import By


class MainPage(Region):
    """Главная страница сайта"""
    conf_lnk = Element(By.CLASS_NAME, 'NavigationPanels-NavSchemeLink__link-hover')
    company_lnk = \
        Element(By.CSS_SELECTOR, '[title="Максимально полный набор возможностей для учета, управлений и коммуникаций"]')
    tool_btn = Element(By.CLASS_NAME, 'controls-Button__text_viewMode-toolButton')
    flag_lang_btn = Element(By.CLASS_NAME, 'engine_LanguageSelector-flagItem')
    ru_lang_btn = Element(By.XPATH, './/div/div/div/div/div/div[2][contains(.,"Русский (Россия)")]')

    def change_conf(self):
        self.conf_lnk.click()
        self.company_lnk.click()

    def set_ru_lang(self):
        self.tool_btn.click()
        self.flag_lang_btn.click()
        self.ru_lang_btn.click()
        delay(1)
