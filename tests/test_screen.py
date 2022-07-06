from atf import *
from atf.ui import *
from pages_inside.libraries.EDWS3.Tasks.taskdialog import Dialog as TaskCard
from pages_inside.edo_controls.edo3dialog import EventTape
from pages_inside.saby_pages.tasks_from_me import TasksFromMe
from pages_inside.login import LoginPage
from pages_inside.libraries.EDO3.timeline import Timeline
from datetime import datetime


class TestTimeLineScreen(TestCaseUI):
    description = 'Тестовое описание задачи от ' + datetime.now().strftime('%H:%M:%S %d.%m.%y')

    @classmethod
    def setUpClass(cls):
        cls.page = TasksFromMe(cls.driver)
        cls.card = TaskCard(cls.driver)
        cls.task = EventTape(cls.driver)
        cls.client = LoginPage(cls.driver).login_with_transit(cls.config.get('LOGIN'), cls.config.get('PASSWORD'))

    def setUp(self):
        self.page.open()
        self.page.add('Задача')
        self.card.fill_task_card(Исполнитель=self.config.get('EXECUTOR_USER_NAME'), Описание=self.description)
        self.card.make_transition()
        delay(1)
        self.card.select_event_tape_tab_by_icon()

    def tearDown(self):
        self.card.delete_task()
        self.browser.close_windows_and_alert()

    def test_01_reg_name_and_icons(self, layout):
        layout.capture(name='reg_name_and_icons', element=self.card.tabs)

    def test_02_timeline_menu(self, layout):
        layout.capture(name='timeline_menu', element=Timeline(self.driver).timeline_head)
