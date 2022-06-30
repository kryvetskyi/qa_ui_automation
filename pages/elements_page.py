import random
import time

from generator.generator import generate_person
from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators
from locators.elements_page_locators import CheckBoxPageLocators


class TestBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generate_person())
        full_name = person_info.full_name
        email = person_info.email
        current_addr = person_info.cur_addr.replace('\n', '')
        permanent_addr = person_info.permanent_addr.replace('\n', '')

        self.is_element_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.is_element_visible(self.locators.EMAIL).send_keys(email)
        self.is_element_visible(self.locators.CURRENT_ADDRESS).send_keys(current_addr)
        self.is_element_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_addr)
        self.scroll_down()
        self.is_element_visible(self.locators.SUBMIT).click()

        return full_name, email, current_addr, permanent_addr

    def check_filled_form(self):
        full_name = self.is_element_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.is_element_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_addr = self.is_element_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_addr = self.is_element_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_addr, permanent_addr


class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.is_element_visible(self.locators.EXPAND_ALL_BUTTON).click()

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

    def get_checked_items(self):
        checked_items = self.are_elements_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_items:
            item_title = box.find_element("xpath", self.locators.ITEM_TITLE)
            data.append(item_title.text)
        return str(data).lower().replace('.doc', '').replace(' ', '')

    def get_success_text_output(self):
        result_list = self.are_elements_present(self.locators.OUTPUT_RESULT)
        items_text = [word.text for word in result_list]
        return str(items_text).lower().replace(' ', '')





