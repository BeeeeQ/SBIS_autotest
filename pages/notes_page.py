# coding=utf-8
from atf.ui import *
from atf.ui.should_be import ExactText
from selenium.webdriver.common.by import By


class NotesPage(Region):
    """Страница Заметки"""
    notes_btn = Element(By.CSS_SELECTOR, '[name="addNote"]')
    note_input_field = TextField(By.CSS_SELECTOR, '[id*="mce"]')
    notes_ok_btn = Element(By.CSS_SELECTOR, '[name="okButton"]')
    my_new_note = Element(By.XPATH, './/p[contains(.,"Клик по элемент c локатором")]')
    erase_btn = Element(By.CSS_SELECTOR, '.icon-24.icon-Erase')
    positive_btn = Element(By.CSS_SELECTOR, '[name="positiveButton"]')

    def opn_add_text_to_note(self, text_of_note):
        self.notes_btn.click()
        self.note_input_field.type_in(text_of_note, clear_txt=False, human=False)
        self.notes_ok_btn.click()

    def del_note(self):
        self.my_new_note.click()
        self.erase_btn.click()
        self.positive_btn.click()


