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
        TasksInWork(cls.driver).open()
        TasksInWork(cls.driver).search_and_open(search_text='Тест линейный не удалять')

    def setUp(self):
        Edo3Dialog(self.driver).double_button.next_phase_click()


    def tearDown(self):
        self.card.dzz.close()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close_windows_and_alert()

    def test_01_dzz_line_process_screen(self, layout):
        layout.capture(name='line_process_dzz_window', element=self.dp.last_item_elm)

    def test_02_dzz_line_process_reassign_screen(self, layout):
        self.card.dzz.transit_to(2, 'Бухгалтер')
        delay(1)
        layout.capture(name='reassign_in_line_process_dzz_window', element=self.dp.last_item_elm)

    def test_03_expand_transitions_dzz_line_process_screen(self, layout):





