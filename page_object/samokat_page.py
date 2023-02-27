from selenium.webdriver.common.by import By

from base_page import BasePage


class MainLocator:
    LOCATOR_Q_1 = (By.XPATH, '//*[@id="accordion__heading-0"]')
    LOCATOR_Q_2 = (By.XPATH, '//*[@id="accordion__heading-1"]')
    LOCATOR_Q_3 = (By.XPATH, '//*[@id="accordion__heading-2"]')
    LOCATOR_Q_4 = (By.XPATH, '//*[@id="accordion__heading-3"]')
    LOCATOR_Q_5 = (By.XPATH, '//*[@id="accordion__heading-4"]')
    LOCATOR_Q_6 = (By.XPATH, '//*[@id="accordion__heading-5"]')
    LOCATOR_Q_7 = (By.XPATH, '//*[@id="accordion__heading-6"]')
    LOCATOR_Q_8 = (By.XPATH, '//*[@id="accordion__heading-7"]')
    LOCATOR_ELEMENT = (By.XPATH, "/html/body/div/div/div/div[5]/div[1]")
    LOCATOR_ORDER_1 = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    LOCATOR_ORDER_2 = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    LOCATOR_SAMOKAT_LOGO = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
    LOCATOR_YA_PAGE = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]')


class MainPage(BasePage):
    #Открытие всех ответов на вопросы
    def check_open_tabs(self):
        element = self.find_element(MainLocator.LOCATOR_ELEMENT)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        seach_element = self.find_element(MainLocator.LOCATOR_Q_1)
        seach_element.click()
        seach_element_1 = self.find_element(MainLocator.LOCATOR_Q_2)
        seach_element_1.click()
        seach_element_2 = self.find_element(MainLocator.LOCATOR_Q_3)
        seach_element_2.click()
        seach_element_3 = self.find_element(MainLocator.LOCATOR_Q_4)
        seach_element_3.click()
        seach_element_4 = self.find_element(MainLocator.LOCATOR_Q_5)
        seach_element_4.click()
        seach_element_5 = self.find_element(MainLocator.LOCATOR_Q_6)
        seach_element_5.click()
        seach_element_6 = self.find_element(MainLocator.LOCATOR_Q_7)
        seach_element_6.click()
        seach_element_7 = self.find_element(MainLocator.LOCATOR_Q_8)
        seach_element_7.click()
    #Клик по верхней кнопке заказа
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








