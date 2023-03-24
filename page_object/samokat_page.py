from selenium.webdriver.common.by import By

from base_page import BasePage

class MainLocator:

    LOCATOR_Q_1 = (By.XPATH, '//[@id="accordion__heading-0"]')
    LOCATOR_Q = (By.ID, "accordion__heading-{}")
    LOCATOR_ASSERT_TEXT = (By.XPATH, "//div[@id='accordion__heading-1']/text()")
    LOCATOR_Q_8 = (By.XPATH, '//*[@id="accordion__heading-7"]')
    LOCATOR_ORDER_1 = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    LOCATOR_ORDER_2 = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    LOCATOR_SAMOKAT_LOGO = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
    LOCATOR_YA_PAGE = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]')
    LOCATOR_FIEND_YA = (By.XPATH, '//button[@type="submit"]')
    LOCATOR_SAMOKAT_PAGE = (By.XPATH, '//div[@class="Home_Header__iJKdX"]')
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    QWES = (By.XPATH, "//*[text()='Вопросы о важном']")


class MainPage(BasePage):
    def check_open_tables(self, num):
        element = self.find_element(MainLocator.LOCATOR_Q_8)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        method, path = MainLocator.LOCATOR_Q
        path = path.format(num)
        import time
        time.sleep(1.3)
        search_element = self.driver.find_element(method, path)
        search_element.click()

    def assertion_text(self, locators):
        import time
        time.sleep(2)
        return self.find_element(By.XPATH, locators)
    # #Клик по верхней кнопке заказа
    def click_to_order_1(self):
        order_button = self.find_element(MainLocator.LOCATOR_ORDER_1)
        order_button.click()
    #Клик по нижней кнопке заказа
    def click_to_order_2(self):
        order_button_2 = self.find_element(MainLocator.LOCATOR_ORDER_2)
        order_button_2.click()
    #Клик по кнопке самоката в топе
    def click_to_samokat_logo(self):
        samokat_logo = self.find_element(MainLocator.LOCATOR_SAMOKAT_LOGO)
        samokat_logo.click()
    #Клик по лого Яндекса
    def click_to_ya_page(self):
        ya_page_logo = self.find_element(MainLocator.LOCATOR_YA_PAGE)
        ya_page_logo.click()

    def assert_ya_page(self):
        result = self.find_element(MainLocator.LOCATOR_YA_PAGE)
        return result.text()

    def asset_samokat_page(self):
        return self.find_element(MainLocator.LOCATOR_SAMOKAT_LOGO).text()

    def remove_cookie(self):
        cookie_button_element = self.find_element(MainLocator.COOKIE_BUTTON)
        cookie_button_element.click()











