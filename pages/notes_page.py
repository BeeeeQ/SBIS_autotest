# coding=utf-8
from atf.ui import *

from selenium.webdriver.common.by import By


class NotesPage(Region):
    """Страница Заметки"""
    notes_btn = Element(By.CSS_SELECTOR, '[name="addNote"]')
    note_input_field = TextField(By.CSS_SELECTOR, '[name = "noteContent"]')

    def opn_add_text_to_note(self, text_of_note):
        self.notes_btn.click()
        self.note_input_field.click()
        self.note_input_field.type_in(text)



