import base64
import os
import random
import time
import allure
import requests

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from generator.generator import generate_person
from locators.elements_page_locators import (
    ButtonsPageLocators,
    CheckBoxPageLocators,
    DownloadPageLocators,
    DynamicPropertiesLocators,
    LinksPageLocators,
    RadioButtonPageLocators,
    TextBoxPageLocators,
    WebTablePageLocators,
)
from pages.base_page import BasePage


class TestBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step("fill in all fields")
    def fill_all_fields(self):
        person_info = next(generate_person())
        full_name = person_info.full_name
        email = person_info.email
        current_addr = person_info.cur_addr.replace("\n", "")
        permanent_addr = person_info.permanent_addr.replace("\n", "")

        with allure.step("fill in persons info fields"):
            self.is_element_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.is_element_visible(self.locators.EMAIL).send_keys(email)
            self.is_element_visible(self.locators.CURRENT_ADDRESS).send_keys(current_addr)
            self.is_element_visible(self.locators.PERMANENT_ADDRESS).send_keys(
                permanent_addr
            )
        self.scroll_down()
        self.is_element_visible(self.locators.SUBMIT).click()

        return full_name, email, current_addr, permanent_addr

    @allure.step("checking filled form")
    def check_filled_form(self):
        full_name = self.is_element_present(self.locators.CREATED_FULL_NAME).text.split(
            ":"
        )[1]
        email = self.is_element_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_addr = self.is_element_present(
            self.locators.CREATED_CURRENT_ADDRESS
        ).text.split(":")[1]
        permanent_addr = self.is_element_present(
            self.locators.CREATED_PERMANENT_ADDRESS
        ).text.split(":")[1]
        return full_name, email, current_addr, permanent_addr


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step("opening full list")
    def open_full_list(self):
        self.is_element_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step("clicking random checkbox")
    def click_random_check_box(self):
        items_list = self.are_elements_visible(self.locators.ITEMS_LIST)

        count = 23
        while count != 0:
            item = items_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.step("getting checked items")
    def get_checked_items(self):
        checked_items = self.are_elements_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_items:
            item_title = box.find_element("xpath", self.locators.ITEM_TITLE)
            data.append(item_title.text)
        return str(data).lower().replace(".doc", "").replace(" ", "")

    @allure.step("getting success text output")
    def get_success_text_output(self):
        result_list = self.are_elements_present(self.locators.OUTPUT_RESULT)
        items_text = [word.text for word in result_list]
        return str(items_text).lower().replace(" ", "")


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step("clicking radio button")
    def click_radio_button(self, choice):
        choices = {
            "yes": self.locators.YES_RADIO_BUTTON,
            "impressive": self.locators.IMPRESSIVE_RADIO_BUTTON,
            "no": self.locators.NO_IMPRESSIVE_RADIO,
        }

        self.is_element_visible(choices[choice]).click()

    @allure.step("getting success text from radio button")
    def get_success_text_output_from_radio_button(self):
        return self.is_element_visible(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    @allure.step("adding new person")
    def add_new_person(self, count=1):
        while count != 0:
            # Generate person info
            person_info = next(generate_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            # Click add button and fill all fields
            self.is_element_visible(self.locators.ADD_BUTTON).click()
            with allure.step("sending person data to fields"):
                self.is_element_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
                self.is_element_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
                self.is_element_visible(self.locators.EMAIL_INPUT).send_keys(email)
                self.is_element_visible(self.locators.AGE_INPUT).send_keys(age)
                self.is_element_visible(self.locators.SALARY_INPUT).send_keys(salary)
                self.is_element_visible(self.locators.DEPARTMENT_INPUT).send_keys(
                    department
                )
            self.is_element_visible(self.locators.SUBMIT).click()
            count -= 1

            return [firstname, lastname, str(age), email, str(salary), department]

    @allure.step("checking added person")
    def check_added_person(self):
        persons_list = self.are_elements_present(self.locators.FULL_PEOPLE_LIST)
        return [person.text.splitlines() for person in persons_list]

    @allure.step("searching some  person")
    def search_some_person(self, person_data):
        window = self.is_element_visible(self.locators.SEARCH_BOX)
        self.go_to_element(window)
        window.send_keys(person_data)

    @allure.step("checking searched person")
    def check_searched_person(self):
        delete_button = self.is_element_visible(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
        self.go_to_element(row)
        return row.text.splitlines()

    @allure.step("updating person")
    def update_person_info(self):
        person_info = next(generate_person())
        age = person_info.age
        self.is_element_visible(self.locators.UPDATE_BUTTON).click()
        self.is_element_visible(self.locators.AGE_INPUT).clear()
        self.is_element_visible(self.locators.AGE_INPUT).send_keys(age)
        self.is_element_visible(self.locators.SUBMIT).click()
        return str(age)

    @allure.step("deleting person")
    def delete_person(self):
        return self.is_element_visible(self.locators.DELETE_BUTTON).click()

    @allure.step("")
    def check_deleted(self):
        return self.is_element_visible(self.locators.NO_ROWS_FOUND).text

    @allure.step("selecting rows")
    def select_rows(self):
        count = [5, 10, 20]
        data = []
        for row in count:
            self.scroll_down()
            select_element = self.is_element_visible(self.locators.COUNT_ROW_LIST)
            select_element.click()
            option_locator = By.XPATH, f'//option[@value="{row}"]'
            self.driver.find_element(*option_locator).click()
            data.append(self.check_count_rows())
        return data

    @allure.step("checking count rows")
    def check_count_rows(self):
        return len(self.are_elements_present(self.locators.FULL_PEOPLE_LIST))


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    @allure.step("clicking different buttons")
    def click_different_buttons(self):
        self.action_double_click(
            self.is_element_visible(self.locators.DOUBLE_CLICK_BUTTON)
        )
        self.action_right_click(
            self.is_element_visible(self.locators.RIGHT_CLICK_BUTTON)
        )
        self.is_element_visible(self.locators.CLICK_ME_BUTTON).click()

    @allure.step("checking button text")
    def check_buttons_text(self):
        first = self.is_element_visible(self.locators.DOUBLE_CLICK_MESSAGE).text
        second = self.is_element_visible(self.locators.RIGHT_CLICK_MESSAGE).text
        last = self.is_element_visible(self.locators.CLICK_ME_MESSAGE).text
        return first, second, last


class LinksPage(BasePage):
    locators = LinksPageLocators()

    @allure.step("checking new tab valid link")
    def check_new_tab_valid_link(self):
        valid_link = self.is_element_visible(self.locators.VALID_HOME_LINK)
        link_href = valid_link.get_attribute("href")
        response = requests.get(f"{link_href}bad")
        if response.status_code == 200:
            valid_link.click()
            self.switch_to_new_tab()
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, f"Status code: {response.status_code}"

    @allure.step("checking broken link")
    def check_broken_link(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            return self.is_element_visible(self.locators.INVALID_LINK)
        else:
            return r.status_code


class DownloadPage(BasePage):
    locators = DownloadPageLocators()

    @allure.step("uploading file")
    def upload_file(self, file):
        return self.is_element_present(self.locators.FILE_INPUT).send_keys(file)

    @allure.step("get uploaded file text")
    def get_uploaded_file_text(self):
        return self.is_element_visible(self.locators.FILE_TEXT).text.split("\\")[-1]

    @allure.step("downloading file")
    def download_file(self, file_path):
        link = self.is_element_present(self.locators.DOWNLOAD_BUTTON).get_attribute(
            "href"
        )
        link = base64.b64decode(link)
        offset = link.find(b"\xff\xd8")

        with open(file_path, "wb") as f:
            f.write(link[offset:])
            check_file = os.path.exists(file_path)
        return check_file


class DynamicProperties(BasePage):
    locators = DynamicPropertiesLocators()

    @allure.step("check if button is enabled")
    def check_button_enabled(self):
        try:
            self.is_element_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

    @allure.step("check if button changed color")
    def check_changed_color(self):
        color_button = self.is_element_present(self.locators.COLOR_CHANGE)
        color_before = color_button.value_of_css_property("color")
        color_button.click()
        time.sleep(5)
        color_after = color_button.value_of_css_property("color")
        return color_before, color_after

    @allure.step("check if  button appears")
    def check_button_appears(self):
        try:
            self.is_element_visible(self.locators.VISIBLE_AFTER)
        except TimeoutException:
            return False
        return True
