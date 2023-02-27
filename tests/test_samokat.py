import allure

from page_object.arenda_page import ArenfaForm
from page_object.oreder_page import OrderPage
from page_object.samokat_page import MainPage


@allure.story("tests")
@allure.feature("test_case")
@allure.step("test Open Objects QBZ")
def test_open_case(browser):

    samokat = MainPage(browser)
    samokat.to_go()
    samokat.check_open_tabs()







