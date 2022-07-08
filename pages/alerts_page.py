import random

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_tab_opened(self):
        self.is_element_visible(self.locators.TAB).click()
        self.switch_to_new_tab()
        return self.is_element_present(self.locators.NEW_TAB).text


class AlertPage(BasePage):
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    TIME_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    PROMPT_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    CONFIRM_RESULT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT_RESULT = (By.CSS_SELECTOR, "span[id='promptResult']")

    def check_see_alert(self):
        self.is_element_visible(self.SEE_ALERT_BUTTON).click()
        return self.driver.switch_to.alert.text

    def check_alert_appears(self):
        self.is_element_visible(self.TIME_ALERT_BUTTON).click()
        time.sleep(5)
        return self.driver.switch_to.alert.text

    def check_confirm_alert(self):
        self.is_element_visible(self.CONFIRM_ALERT_BUTTON).click()
        self.driver.switch_to.alert.accept()
        return self.is_element_present(self.CONFIRM_RESULT).text

    def check_confirm_prompt(self):
        text = f'autotest-{random.randint(1, 100)}'
        self.is_element_visible(self.PROMPT_ALERT_BUTTON).click()
        modal = self.driver.switch_to.alert
        modal.send_keys(text)
        modal.accept()
        text_result = self.is_element_present(self.PROMPT_RESULT).text
        return text, text_result
