from atf.ui import *
from pages_inside.libraries.EDWS3.Tasks.taskdialog import Dialog as TaskCard
from pages_inside.saby_pages.tasks_from_me import TasksFromMe
from pages_inside.documents.notes.index import NoteEdit
from pages_inside.login import LoginPage
from pages_inside.tasks.tasks.functions import create_task_by_post, post_delete_docs_by_id
from datetime import datetime


class TestNoteOnTask(TestCaseUI):
    description = 'Тестовое описание задачи от ' + datetime.now().strftime('%H:%M:%S %d.%m.%y')
    note_text = 'Текст заметки от ' + datetime.now().strftime('%H:%M:%S %d.%m.%y')
    note_text1 = 'Changed'
    task_id = None
    client = None

    @classmethod
    def setUpClass(cls):
        cls.page = TasksFromMe(cls.driver)
        cls.card = TaskCard(cls.driver)
        cls.note = NoteEdit(cls.driver)
        cls.client = LoginPage(cls.driver).login_with_transit(cls.config.get('LOGIN'), cls.config.get('PASSWORD'))
        cls.task_id = create_task_by_post(cls.client, cls.config.get('EXECUTOR_USER_NAME'), cls.description,
                                          regulation='Задача')

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        post_delete_docs_by_id(cls.client, [cls.task_id], forever=True)
        cls.browser.close_windows_and_alert()

    def test_01_create_note_on_task(self):
        """Открываем созданную задачу, добавляем заметку, сохраняем, проверяем отображение"""
        self.page.open()
        card = self.card
        note = self.note
        self.page.search_and_open(search_text=self.description)
        card.service_commands.select_service_command('Пометки и заметки')
        card.marks.marks_dialog.add_note()
        note.enter_text_in_editor(note_text=self.note_text)
        note.save()
        card.check_notes(count=1)

    def test_02_edit_note_on_task(self):
        """Редактируем заметку, сохраняем, проверяем отображение"""
        card = self.card
        note = self.note
        card.notes_cslst.click()
        note.enter_text_in_editor(note_text=self.note_text1, check_placeholder=False)
        note.save()
        card.check_notes_text(self.note_text1)

    def test_03_delete_note_on_task(self):
        """Удаляем заметку, проверяем, что заметок на доке нет"""
        card = self.card
        card.notes_cslst.click()
        self.note.delete_note()
        card.check_notes(count=0)
