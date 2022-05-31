from pages_inside.edo_controls.saby_page import SabyPage
from pages_inside.edo_controls.edo3dialog import ServiceCommands
from pages_inside.saby_pages.milestones import Milestones
from pages_inside.libraries.PM.Milestones.dialog import CreateMilestoneCard
from datetime import datetime


class PlansAndDeadlines(SabyPage):

    milestone_name = 'Test_Milestone_name_' + datetime.now().strftime('%H:%M:%S_%d.%m.%y')
    milestone_description = 'Test_Milestone_description_' + datetime.now().strftime('%H:%M:%S_%d.%m.%y')

    def open_milestone_tab(self):
        Milestones(self.driver).open_registry()
        Milestones(self.driver).go_to_milestone_registry()

    def create_new_milestone(self):
        Milestones(self.driver).add_milestone(
            {'Название': self.milestone_name, 'Описание': self.milestone_description}, 'Выпуск релиза')

    def open_new_milestone(self):
        Milestones(self.driver).select_milestone(milestone_name=self.milestone_name)

    def check_new_milestone_data(self):
        CreateMilestoneCard(self.driver).check_milestone_data(
            {'Название': self.milestone_name, 'Описание': self.milestone_description})

    def check_new_window_milestone_data(self):
        CreateMilestoneCard(self.driver).open_new_tab(switch_to_new=True)
        CreateMilestoneCard(self.driver).check_milestone_data(
            {'Название': self.milestone_name, 'Описание': self.milestone_description})

    def delete_new_milestone(self):
        ServiceCommands(self.driver).delete()
