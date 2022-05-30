from atf.ui import *
from pages_inside.left_accordeon import LeftAccordeon
from pages_inside.saby_pages.tasks_from_me import TasksFromMe


class LeftAccordeonOpnPart(Region):

    def opn_plans_and_deadlines(self):
        LeftAccordeon(self.driver).move_to_section_click('Задачи', 'Планы и сроки')

    def opn_tasks_from_me(self):
        TasksFromMe(self.driver).open()
