from pages.alerts_page import BrowserWindowsPage, AlertPage


class TestAlertFrameWindow:
    class TestBrowserWindows:

        def test_new_tab(self, driver):
            tab = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            tab.open()
            title = tab.check_tab_opened()
            assert title == 'This is a sample page', 'New tab was not open or title is not present.'

        def test_new_window(self, driver):
            window = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            window.open()
            title = window.check_tab_opened()
            assert title == 'This is a sample page', 'New tab was not open or title is not present.'

    class TestAlert:

        def test_check_see_alert(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button'

        def test_check_alert_appears(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appears()
            assert alert_text == 'This alert appeared after 5 seconds'

        def test_check_confirm_result(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok'

        def test_check_confirm_prompt(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text_to_send, result_text = alert_page.check_confirm_prompt()
            assert text_to_send in result_text

