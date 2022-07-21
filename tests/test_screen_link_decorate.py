from atf import *
from atf.ui import *
from atf.ui import Element
from pages_inside.libraries.EDO3.timeline import CurrentStateDialog
from pages_inside.libraries.EDO3.timeline import Timeline
from pages_inside.libraries.EDWS3.Tasks.taskdialog import Dialog as TaskCard
from pages_inside.edo_controls.edo3dialog import EventTape, Edo3Dialog
from pages_inside.saby_pages.tasks_in_work import TasksInWork
from pages_inside.login import LoginPage
from pages_inside.documents.index import DocsPage
from pages_inside.tasks.tasks.functions import create_task_by_post, post_delete_docs_by_id
from datetime import datetime


class TestDecorateLink(TestCaseUI):
    description = 'Тестовое описание задачи от ' + datetime.now().strftime('%H:%M:%S %d.%m.%y')
    client = None
    task_id = None

    @classmethod
    def setUpClass(cls):
        cls.client = LoginPage(cls.driver).login_with_transit(cls.config.get('LOGIN'), cls.config.get('PASSWORD'))
        cls.page = TasksInWork(cls.driver)
        cls.card = TaskCard(cls.driver)
        cls.feed = Timeline(cls.driver)
        cls.cs = CurrentStateDialog(cls.driver)
        cls.dp = DocsPage(cls.driver)

    def setUp(self):
        self.page.open()
        self.page.search_and_open(search_text='Тест декорирования не удалять')
        self.card.select_event_tape_tab_by_icon()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.browser.close_windows_and_alert()

    def test_01_decorate_in_current_state(self, layout):
        self.feed.chat.click()
        delay(3)
        layout.capture(name='current_state_window', element=self.cs.current_state_window)

    def test_02_check_decorate_in_dzz(self, layout):
        self.card.next_phase_click()
        delay(3)
        layout.capture(name='dzz_attach', element=self.dp.last_item_elm)

