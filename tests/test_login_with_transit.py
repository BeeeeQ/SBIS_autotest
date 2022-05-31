import pytest
from atf import *
from atf.ui import *
from atf.api import *
import random
from datetime import datetime
from pages_inside.login import LoginPage
from pages_inside.saby_pages.tasks_from_me import TasksFromMe
from pages_inside.saby_pages.tasks_in_work import TasksInWork
from pages_inside.libraries.EDWS3.Tasks.taskdialog import Dialog as TaskCard

class TestLoginWithTransit(TestCaseUI):
    url = Config().get('SITE')
    login = Config().get('LOGIN')
    password = Config().get('PASSWORD')
    task_description = 'Task Description'

    @classmethod
    def setUpClass(cls):
        cls.client = JsonRpcClient(url=cls.url)
        cls.client.auth(cls.login, cls.password)
        LoginPage(cls.driver).login_with_transit(cls.login, cls.password, 'Задачи')
        cls.on_me = TasksInWork(cls.driver)
        cls.card = TaskCard(cls.driver)

    def setUp(self):


    def tearDown(self):


    def test_01(self):
