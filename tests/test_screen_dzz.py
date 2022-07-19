from atf import *
from atf.ui import *
from pages_inside.libraries.EDWS3.Tasks.taskdialog import Dialog as TaskCard
from pages_inside.edo_controls.edo3dialog import EventTape, Edo3Dialog
from pages_inside.saby_pages.tasks_from_me import TasksFromMe
from pages_inside.login import LoginPage
from pages_inside.tasks.tasks.functions import create_task_by_post, post_delete_docs_by_id
from pages_inside.libraries.EDO3.timeline import Timeline
from datetime import datetime


class TestDZZ(TestCaseUI):
    description = 'Тестовое описание задачи от ' + datetime.now().strftime('%H:%M:%S %d.%m.%y')
    client = None
    task_id = None

    @classmethod
    def setUpClass(cls):
        cls.page = TasksFromMe(cls.driver)
        cls.card = TaskCard(cls.driver)
        cls.feed = EventTape(cls.driver)
        cls.task = Edo3Dialog(cls.driver)
        cls.client = LoginPage(cls.driver).login_with_transit(cls.config.get('LOGIN'), cls.config.get('PASSWORD'))
        cls.task_id = create_task_by_post(cls.client, cls.config.get('EXECUTOR_USER_NAME'), cls.description,
                                          regulation='Задача')
        TasksFromMe(cls.driver).open()
        TasksFromMe(cls.driver).search_and_open(search_text=cls.description)
        Edo3Dialog(cls.driver).change_doc_lnk.click()
        delay(1)
        Edo3Dialog(cls.driver).dn.set_date('06.07.22')
        Edo3Dialog(cls.driver).dn.set_number('446')

    def setUp(self):
        Edo3Dialog(self.driver).double_button.next_phase_click()

    def tearDown(self):
        self.card.dzz.close()

    @classmethod
    def tearDownClass(cls):
        post_delete_docs_by_id(cls.client, [cls.task_id], forever=True)
        cls.browser.close_windows_and_alert()

    def test_01_passage_elm(self, layout):
        layout.capture(name='passage_elm', element=self.card.dzz.passage_elm)

    def test_02_choose_staff_for_reassign(self, layout):
        self.card.dzz.transit_to(2, 'Бухгалтер')
        delay(1)
        layout.capture(name='passage_elm', element=self.card.dzz.passage_elm)

    def test_03_dzz_settings(self, layout):
        self.card.dzz.passage_settings_btn.click()
        delay(1)
        layout.capture(name='passage_settings_window', element=self.card.dzz.passage_settings.panel)

