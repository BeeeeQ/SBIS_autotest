from atf import *
from atf.ui import *
from pages_inside.left_accordeon import LeftAccordeon


class LeftAccordeonOpnPart(Region):

    def opn_plans_and_deadlines(self):
        LeftAccordeon(self.driver).move_to_section_click('Задачи', 'Планы и сроки')
