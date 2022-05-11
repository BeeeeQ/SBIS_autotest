from atf import *
from atf.ui import *


class NewTest(TestCaseUI):
    @classmethod
    def setup_class(cls):
        cls.browser.open('https://fix-online.sbis.ru/auth/')
        AuthPage(cls.driver).auth('Демо_тензор', 'Демо123')


    def setup(self):
        MainPage(self.driver).search.should_be(Displayed, wait_time=True)


    def test_01_open_news(self):
        MainPage(self.driver).search_and_open_news('Новость для автотеста')


    def test_02_text_in_news(self):
        MainPage(self.driver).check_text_by_title(title_news='Новость для автотеста', text_news='Не удаляйте')


    def teardown(self):
            self.browser.close_windows_and_alert()


if __name__ == '__main__':
    run_tests()

