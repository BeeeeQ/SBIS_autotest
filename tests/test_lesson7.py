from atf import *
from atf.ui import *
from pages_inside import *
from pages_inside.libraries.AuthControls.authForm import Adaptive
from pages.left_accordeon_page import LeftAccordeonOpnPart
from pages.plans_and_deadlines_page import PlansAndDeadlines


class TestMilestoneCreate(TestCaseUI):
    @classmethod
    def setUpClass(cls):
        cls.browser.open('https://fix-online.sbis.ru/auth/')
        Adaptive(cls.driver).login_as('бот', 'БотА12')

    def setUp(self):
        LeftAccordeonOpnPart(self.driver).opn_plans_and_deadlines()
        PlansAndDeadlines(self.driver).open_milestone_tab()

    def test_01_create_new_milestone(self):
        PlansAndDeadlines(self.driver).create_new_milestone()
        delay(3)

    def tearDown(self):
        self.browser.close_windows_and_alert()
