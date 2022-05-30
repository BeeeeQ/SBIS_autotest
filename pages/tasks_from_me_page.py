from atf.ui import *
from pages_inside.edo_controls.saby_page import SabyPage
from pages_inside.libraries.EDWS3.Tasks.taskdialog import Dialog
from datetime import datetime
from pages_inside.edo_controls.edo3dialog import Edo3Dialog
from pages_inside.edo_controls.edo3dialog import ServiceCommands
from pages_inside.libraries.EDWS3.Tasks.MasterDetail import MasterDetail
from pages_inside.libraries.EDO3.Marks.Dialog import MarksDialog
from pages_inside.documents.notes.index import NoteEdit


class TasksFromMePage(SabyPage):
    executor = 'Бухгалтер Галина Геннадьевна'
    description = 'Тестовое описание задачи от ' + datetime.now().strftime('%H:%M:%S %d.%m.%y')
    note_text = 'Текст заметки от ' + datetime.now().strftime('%H:%M:%S %d.%m.%y')
    note_text1 = 'Changed'
    note = NoteEdit(TestCaseUI.driver)
    e3d = Edo3Dialog(TestCaseUI.driver)
    sc = ServiceCommands(TestCaseUI.driver)

    def create_task_fill_and_save(self):
        dialog = Dialog(self.driver)
        SabyPage(self.driver).add('Задача')
        dialog.fill_task_card(Исполнитель=self.executor, Описание=self.description)
        dialog.check_fields()
        dialog.make_transition(close=True)
        # dialog.close(confirmation_btn='Да') Если потребуется закрыть без сохранения

    def opn_new_task_and_add_note(self):

        MasterDetail(self.driver).search_and_open(search_text=self.description)
        self.sc.select_service_command('Пометки и заметки')
        MarksDialog(self.driver).add_note()
        self.note.enter_text_in_editor(note_text=self.note_text)
        self.note.save()
        self.e3d.check_notes(count=1)

    def note_edit(self):
        self.e3d.notes_cslst.click()
        self.note.enter_text_in_editor(note_text=self.note_text1, check_placeholder=False)
        self.note.save()
        self.e3d.check_notes_text(self.note_text1)

    def delete_note(self):
        self.e3d.notes_cslst.click()
        self.note.delete_note()
        self.e3d.check_notes(count=0)

    def delete_task(self):
        self.sc.delete()
