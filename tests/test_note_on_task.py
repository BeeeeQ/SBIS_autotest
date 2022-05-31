from atf.ui import *
from pages_inside.libraries.AuthControls.authForm import Adaptive
from pages.left_accordeon_page import LeftAccordeonOpnPart
from pages_inside.saby_pages.tasks_from_me import TasksFromMe
from pages.tasks_from_me_page import TasksFromMePage


class TestNoteOnTask(TestCaseUI):
    @classmethod
    def setUpClass(cls):
        cls.task = TasksFromMePage(cls.driver)
        cls.browser.open('https://fix-online.sbis.ru/auth/')
        Adaptive(cls.driver).login_as('бот', 'БотА12')

    def setUp(self):
        LeftAccordeonOpnPart(self.driver).opn_tasks_from_me()
        TasksFromMe(self.driver).select_tab('Список')

    def test_01_create_task_and_note(self):
        """Создание задачи, запуск в ДО, добавление и редактирование заметки, проверка отображения и удаление заметки"""
        self.task.create_task_fill_and_save()
        self.task.opn_new_task_and_add_note()
        self.task.note_edit()
        self.task.delete_note()

    def tearDown(self):
        self.task.delete_task()
        self.browser.close_windows_and_alert()
