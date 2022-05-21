from atf import *
from atf.ui import *
from pages_inside.edo_controls.saby_page import SabyPage


class PlansAndDeadlines(Region):

    def open_milestone_tab(self):
        SabyPage().select_tab('Вехи и сроки')
