# -*- coding: utf-8 -*-
from atf import *
from atf.ui import *
from selenium.webdriver.common.by import By


class LoginPage(Region):
    """Страница аутентификации """

    login_inp = TextField(By.NAME, 'Login', 'Логин')
    psw_inp = TextField(By.NAME, 'Password', 'Пароль')
    login_btn = Button(By.CLASS_NAME, 'controls-Button__wrapper_button_4xl', 'Войти')

    def login_as(self, username, password):
        """Авторизация
        :param username - логин
        :param password - пароль"""

        delay(1)
        self.login_inp.click()
        self.login_inp.type_in(username)
        self.login_inp.should_be(ExactText(username), msg='Логин не ввелся')
        delay(1)
        self.login_btn.click()
        self.psw_inp.type_in(password)
        delay(1)
        self.login_btn.click()


