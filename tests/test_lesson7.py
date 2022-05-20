from atf import *
from atf.ui import *
from pages_inside import *
from pages_inside.libraries.AuthControls.authForm import Adaptive
from pages_inside.left_accordeon import LeftAccordeon
from atf.ui.controls_vdom import ControlsTabsButtons


class TestMilestoneCreate(TestCaseUI):
    @classmethod
    def setUpClass(cls):
        cls.browser.open('https://fix-online.sbis.ru/auth/')
        Adaptive(cls.driver).login_as('бот', 'БотА12')

    def setUp(self):
        LeftAccordeon(self.driver).move_to_section_click('Задачи', 'Планы и сроки')
        ControlsTabsButtons(self.driver).select(with_text='Вехи и сроки')
        delay(3)

    def test_01_create_note(self):
        pass

    def tearDown(self):
        self.browser.close_windows_and_alert()
