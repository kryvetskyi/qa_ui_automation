from pages.alerts_page import BrowserWindowsPage


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
