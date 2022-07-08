from atf import *
from atf.ui import *
from pages_inside.libraries.EDWS3.Tasks.taskdialog import Dialog as TaskCard
from pages_inside.edo_controls.edo3dialog import EventTape, Edo3Dialog
from pages_inside.saby_pages.tasks_from_me import TasksFromMe
from pages_inside.login import LoginPage
from pages_inside.tasks.tasks.functions import create_task_by_post, post_delete_docs_by_id
from pages_inside.libraries.EDO3.timeline import Timeline
from datetime import datetime


class TestTimeLineScreen(TestCaseUI):
    # task_head = Element(By.CSS_SELECTOR, '.controls-StackTemplate__top-area')
    description = 'Тестовое описание задачи от ' + datetime.now().strftime('%H:%M:%S %d.%m.%y')
    client = None
    task_id = None
    # dzz_card = Element(By.CLASS_NAME, Edo3Dialog.last_panel_class)

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
        Edo3Dialog(cls.driver).select_event_tape_tab_by_icon()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        post_delete_docs_by_id(cls.client, [cls.task_id], forever=True)
        cls.browser.close_windows_and_alert()

    def test_01_reg_name_and_icons(self, layout):
        layout.capture(name='reg_name_and_icons', element=self.card.tabs)

    def test_02_timeline_menu(self, layout):
        layout.capture(name='timeline_menu', element=Timeline(self.driver).timeline_head)



