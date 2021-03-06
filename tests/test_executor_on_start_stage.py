from atf import *
from atf.ui import *
from pages_inside.libraries.EDWS3.Tasks.taskdialog import Dialog as TaskCard
from pages_inside.edo_controls.edo3dialog import EventTape
from pages_inside.saby_pages.tasks_from_me import TasksFromMe
from pages_inside.login import LoginPage
from datetime import datetime
from helpers.layout import Layout


class TestExecutorOnStartStage(TestCaseUI):
    description = 'Тестовое описание задачи от ' + datetime.now().strftime('%H:%M:%S %d.%m.%y')
    regulation = ['старт исполнитель определен (бот)', 'старт исполнитель не определен',
                  '2 этапа оба определены (бот и сваркин)', '2 этапа (бот и неопределен)', '2 этапа оба неопределены',
                  '2 этапа и два перехода оба определены (бот и сваркин)']
    reg_num = 0
    task_id = None
    client = None

    @classmethod
    def setUpClass(cls):
        cls.page = TasksFromMe(cls.driver)
        cls.card = TaskCard(cls.driver)
        cls.task = EventTape(cls.driver)
        cls.client = LoginPage(cls.driver).login_with_transit(cls.config.get('LOGIN'), cls.config.get('PASSWORD'))

    def setUp(self):
        self.page.open()
        self.page.add(self.regulation[self.reg_num])
        TestExecutorOnStartStage.reg_num += 1
        self.card.fill_task_card(Исполнитель=self.config.get('EXECUTOR_USER_NAME'), Описание=self.description)

    def tearDown(self):
        self.card.delete_task()
        self.browser.close_windows_and_alert()

    def test_01_executor_determined(self, layout):
        """Исполнитель на старте определен, проверяем правильность выбора"""
        self.card.make_transition()
        delay(1)
        self.card.select_event_tape_tab_by_icon()
        log('Проверяем исполнителя активного этапа')
        self.task.check_current_responsible(self.config.get('EXECUTOR_USER_NAME_IN_FEED'))

    def test_02_performer_need_to_choose(self):
        """Исполнитель на старте выбирается вручную"""
        self.card.next_phase_btn.click()
        self.card.dzz.executor_fl.autocomplete_search(self.config.get('EXECUTOR_USER_NAME'))
        self.card.dzz.click_on_transit_by_title('старт')
        delay(1)
        self.card.select_event_tape_tab_by_icon()
        log('Проверяем исполнителя активного этапа')
        self.task.check_current_responsible(self.config.get('EXECUTOR_USER_NAME_IN_FEED'))

    def test_03_two_performers_is_selected(self):
        """Два исполнителя определены на старте"""
        self.card.make_transition()
        delay(1)
        self.card.select_event_tape_tab_by_icon()
        log('Проверяем исполнителя активного этапа')
        self.task.check_event('Бот А.А.', num_phase=2)
        self.task.check_event('Сваркин С.Г.', num_phase=3)

    def test_04_two_performers_one_need_to_choose(self):
        """Два этапа на старте, на одном исполнитель выбирается вручную"""
        self.card.next_phase_btn.click()
        self.card.dzz.executor_fl.autocomplete_search('Бухгалтер Галина Геннадьевна')
        self.card.dzz.click_on_transit_by_title('старт1, старт2')
        delay(1)
        self.card.select_event_tape_tab_by_icon()
        log('Проверяем исполнителя активного этапа')
        self.task.check_event('Бот А.А.', num_phase=2)
        self.task.check_event('Бухгалтер Г.Г.', num_phase=3)

    def test_05_need_to_choose_two_performers(self):
        """Два этапа на старте, на обоих исполнитель выбирается вручную"""
        self.card.next_phase_btn.click()
        self.card.dzz.executor_fl.autocomplete_search('Бот Алексей Алексеевич')
        self.card.dzz.executor_fl.autocomplete_search('Бухгалтер Галина Геннадьевна')
        self.card.dzz.click_on_transit_by_title('старт1, старт2')
        delay(1)
        self.card.select_event_tape_tab_by_icon()
        log('Проверяем исполнителя активного этапа')
        self.task.check_event('Бот А.А.', num_phase=2)
        self.task.check_event('Бухгалтер Г.Г.', num_phase=3)
