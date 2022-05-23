from atf import *
from atf.ui import *
from pages_inside.edo_controls.saby_page import SabyPage
from selenium.webdriver.common.by import By
from pages_inside.edo_controls.edo3dialog import Edo3Dialog
from atf.ui.controls_vdom.vdom_controls_text_editor_base import TextEditorBaseEditor
from pages_inside.saby_pages.milestones import Milestones


class PlansAndDeadlines(SabyPage):

    def open_milestone_tab(self):
        self.select_tab('Вехи и сроки')
        self.check_current_tab('Вехи и сроки')

    def create_new_milestone(self):
        Milestones(self.driver).add_milestone({'Название': 'Test_Milestone_name_123456', 'Описание': 'Test_Milestone_description_123456_'}, 'Выпуск релиза')
