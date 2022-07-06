from atf import *
from atf.ui import *
from pages_inside.libraries.EDWS3.Tasks.taskdialog import Dialog as TaskCard
from pages_inside.edo_controls.edo3dialog import EventTape
from pages_inside.saby_pages.tasks_from_me import TasksFromMe
from pages_inside.login import LoginPage
from datetime import datetime
from pages_inside.libraries.EDO3.timeline import CurrentStateDialog
import random


class TestExecutorOnStartStage(TestCaseUI):
    description = 'Тестовое описание задачи от ' + datetime.now().strftime('%H:%M:%S %d.%m.%y')

    @classmethod
    def setUpClass(cls):
        cls.page = TasksFromMe(cls.driver)
        cls.card = TaskCard(cls.driver)
        cls.task = EventTape(cls.driver)
        cls.client = LoginPage(cls.driver).login_with_transit(cls.config.get('LOGIN1'), cls.config.get('PASSWORD1'))

    def setUp(self):
        self.page.open()


        delay(10)
        self.card.select_event_tape_tab_by_icon()

    def tearDown(self):
        self.browser.close_windows_and_alert()

    def test_01_set_current_state(self, subtests):
        """Выставление текущего состояния"""

        log('Выставление текущего состояния')
        task = self.card
        event_tape = task.select_event_tape_tab()
        event_tape.check_load()
        cur_state = CurrentStateDialog(self.driver)
        for i in range(750):
            self.description += str(random.randint(0, 9))
            with subtests.test():
                event_tape.select_option('Текущее состояние по документу')
                cur_state.set_current_state(self.description)
                delay(1)

