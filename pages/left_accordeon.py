# coding=utf-8
from atf.ui import *

from selenium.webdriver.common.by import By


class LeftAccordeon(Region):
    """Левый аккордеон"""
    documents_btn = Element(By.CSS_SELECTOR, '[data-qa="Документы"]')
    notes_btn = Element(By.CSS_SELECTOR, '[data-qa="Заметки"]')

    def open_notes_chapter(self):
        LeftAccordeon(self.driver).documents_btn.click()
        LeftAccordeon(self.driver).notes_btn.click()
