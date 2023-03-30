import allure
import pytest
from page_object.samokat_page import MainPage


class TestOpenTabs:
    @allure.story("tests")
    @allure.feature("test_case")
    @pytest.mark.parametrize("num", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_for_damir(self, browser, num):
        samokat = MainPage(browser)
        samokat.to_go()
        samokat.remove_cookie()
        samokat.check_open_tables(num)







