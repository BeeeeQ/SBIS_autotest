from atf import *
from atf.ui import *
from pages.auth_page import LoginPage
from pages.main_page import MainPage
from pages.left_accordeon import LeftAccordeon
from pages.notes_page import NotesPage
from atf.ui.should_be import Enabled
from atf.ui.should_be import ExactText


class TestNewTest(TestCaseUI):
    @classmethod
    def setUpClass(cls):
        cls.browser.open('https://fix-online.sbis.ru/auth/')
        LoginPage(cls.driver).login_as('бот', 'БотА12')

    def setUp(self):
        MainPage(self.driver).conf_lnk.should_be(Enabled)
        MainPage(self.driver).set_ru_lang()
        MainPage(self.driver).change_conf()

    def test_01_create_note(self):
        LeftAccordeon(self.driver).open_notes_chapter()
        NotesPage(self.driver).opn_add_text_to_note('Клик по элемент c локатором')
        ExactText(self.driver).match(NotesPage.my_new_note)
        NotesPage(self.driver).del_note()

    def tearDown(self):
        self.browser.close_windows_and_alert()
