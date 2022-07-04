import random
import time

from pages.elements_page import (
    TestBoxPage,
    ButtonsPage,
    CheckBoxPage,
    RadioButtonPage,
    WebTablePage,
    LinksPage,
)


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

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()

            radio_button_page.click_radio_button('yes')
            yes = radio_button_page.get_success_text_output_from_radio_button()

            radio_button_page.click_radio_button('impressive')
            impressive = radio_button_page.get_success_text_output_from_radio_button()

            radio_button_page.click_radio_button('no')
            no = radio_button_page.get_success_text_output_from_radio_button()

            assert yes == 'Yes', 'Yes have not been selected'
            assert impressive == 'Impressive', 'Impressive have not been selected'
            assert no == 'No', 'No have not been selected'

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            created_person = web_table_page.add_new_person()
            time.sleep(2)
            all_persons = web_table_page.check_added_person()

            assert created_person in all_persons

        def test_web_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            firstname = web_table_page.add_new_person()[random.randint(1, 5)]
            web_table_page.search_some_person(firstname)
            searched_result = web_table_page.check_searched_person()

            assert firstname in searched_result, 'Person was not found'

        def test_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            # create person and get last name
            lastname = web_table_page.add_new_person()[1]
            # search created person by name
            web_table_page.search_some_person(lastname)
            # update person age
            age = web_table_page.update_person_info()
            # search same person after update
            row = web_table_page.check_searched_person()

            assert age in row, 'Person data was not updated.'

        def test_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()

            # create person and get email
            email = web_table_page.add_new_person()[3]
            # search created person by email
            web_table_page.search_some_person(email)
            # delete person
            web_table_page.delete_person()
            # search same person after delete
            row = web_table_page.check_deleted()

            assert row == 'No rows found', 'Person was not deleted.'

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            result = web_table_page.select_rows()
            assert result == [5, 10, 20, 25, 50, 100], 'Count rows were not changed.'

    class TestButtonsPage:

        def test_buttons_page(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            buttons_page.click_different_buttons()
            result = buttons_page.check_buttons_text()

            assert result[0] == 'You have done a double click', 'Double click was not performed.'
            assert result[1] == 'You have done a right click', 'Right click was not performed.'
            assert result[2] == 'You have done a dynamic click', 'Click was not performed.'

    class TestLinkPage:

        def test_check_valid_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href, cur_url = links_page.check_new_tab_valid_link()
            assert href == cur_url

        def test_check_invalid_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            url = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert url == 400


