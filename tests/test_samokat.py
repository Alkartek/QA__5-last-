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
    samokat.open_element_1()


@allure.step("test order_form")
def test_oreder(browser):

    samokat_order = MainPage(browser)
    samokat_order.to_go()
    samokat_order.click_to_order_1()
    order_form = OrderPage(browser)
    order_form.input_elements(ima="Дамир", familia="Исаков", street="Улица")
    order_form.click_to_next()
    page_order_second = ArenfaForm(browser)
    page_order_second.from_element()
    page_order_second.form_oder_button()
    page_order_second.last_order_accept()



@allure.step("test order_form_2")
def test_order_second(browser):

    samokat_order = MainPage(browser)
    samokat_order.to_go()
    samokat_order.click_to_order_1()
    order_form = OrderPage(browser)
    order_form.input_elements(ima="имя", familia="фамилия", street="стриит")
    order_form.click_to_next()
    page_order_second = ArenfaForm(browser)
    page_order_second.from_element()
    page_order_second.form_oder_button()
    page_order_second.last_order_accept()


@allure.step("test_to_go_in_logo")
def test_main_logo(browser):

    samokat_page = MainPage(browser)
    samokat_page.to_go()
    samokat_page.click_to_order_1()
    samokat_page.click_to_samokat_logo()
    samokat_page.click_to_ya_page()






