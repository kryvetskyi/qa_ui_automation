from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def is_element_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator)
        )

    def are_elements_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(
            ec.visibility_of_all_elements_located(locator)
        )

    def is_element_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def are_elements_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(
            ec.presence_of_all_elements_located(locator)
        )

    def is_element_invisible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(
            ec.invisibility_of_element_located(locator)
        )

    def is_element_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element).perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    def remove_footer(self):
        self.driver.execute_script(
            "document.getElementsByTagName('footer')[0].remove();"
        )
        self.driver.execute_script(
            "document.getElementById('close-fixedban').remove();"
        )
        self.driver.execute_script(
            "document.getElementsByTagName('iframe')[0].remove();"
        )

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
