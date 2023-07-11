from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from datetime import datetime
from pathlib import Path


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def is_element_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def are_elements_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def is_element_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def are_elements_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def is_element_invisible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def is_element_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

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

    def capture_screenshot(self):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_filename = f"screenshot_{timestamp}.png"
        screenshot_dir = Path(__file__).resolve().parent / '..' / 'screenshots'
        screenshot_dir.mkdir(parents=True, exist_ok=True)
        screenshot_path = screenshot_dir / screenshot_filename
        self.driver.get_screenshot_as_file(screenshot_path)

