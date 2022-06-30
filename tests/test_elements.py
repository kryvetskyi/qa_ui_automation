import time

from pages.elements_page import TestBoxPage
from pages.elements_page import CheckBoxPage


class TestElements:

    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TestBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()

            full_name, email, current_addr, permanent_addr = text_box_page.fill_all_fields()
            output_fullname, output_email, output_cur_addr, output_perm_addr = text_box_page.check_filled_form()

            assert full_name == output_fullname, 'full_name does not match.'
            assert email == output_email, 'Email does not match.'
            assert current_addr == output_cur_addr, 'Current address does not match.'
            assert permanent_addr == output_perm_addr, 'Permanent address does not match.'

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_check_box()
            input_checkboxes = check_box_page.get_checked_items()
            output_checkboxes = check_box_page.get_success_text_output()

            assert input_checkboxes == output_checkboxes, 'Checkboxes were not selected.'
