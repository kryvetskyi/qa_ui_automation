from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_tab_opened(self):
        self.is_element_visible(self.locators.TAB).click()
        self.switch_to_new_tab()
        return self.is_element_present(self.locators.NEW_TAB).text

