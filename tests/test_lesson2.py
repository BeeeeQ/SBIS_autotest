
from atf import *
from atf.ui import *
from pages.auth_page import LoginPage
from pages.main_page import MainPage
from pages.left_accordeon import LeftAccordeon
from pages.notes_page import NotesPage
from atf.ui.should_be import Enabled


class TestNewTest(TestCaseUI):
    @classmethod
    def setUpClass(cls):
        cls.browser.open('https://fix-online.sbis.ru/auth/')
        LoginPage(cls.driver).login_as('Демо_тензор', 'Демо123')

    def setUp(self):
        MainPage(self.driver).conf_lnk.should_be(Enabled)
        MainPage(self.driver).change_conf()

    def test_01_create_note(self):
        LeftAccordeon(self.driver).documents_btn.click()
        LeftAccordeon(self.driver).notes_btn.click()
        NotesPage(self.driver).opn_add_text_to_note('Клик по элемент c локатором "NavigationPanels-NavSchemeLink__link-hover"')

    def teardown(self):
        self.browser.close_windows_and_alert()
