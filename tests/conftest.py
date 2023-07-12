from datetime import datetime
import os
import random
from pathlib import Path

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome", help="Enter browser")
    parser.addoption("--headless", action="store", default="headless", help="Run tests in headless mode")


@pytest.fixture(scope='function')
def driver(request):
    browser = request.config.getoption("--driver")
    if browser != 'chrome':
        pytest.fail('only chrome is supported at the moment')

    headless = request.config.getoption("--headless")
    options = Options()
    options.add_argument("--start-maximized")
    if headless:
        options.add_argument(headless)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver

    if request.node.rep_call.failed:
        screenshot_filename, screenshot_path = create_screenshot_path()
        allure.attach(driver.get_screenshot_as_file(screenshot_path),
                      name=screenshot_filename,
                      attachment_type=allure.attachment_type.PNG)

    driver.quit()


def create_screenshot_path():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_filename = f"screenshot_{timestamp}.png"
    screenshot_dir = Path(__file__).resolve().parent.parent / 'reports' / 'screenshots'
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    screenshot_path = screenshot_dir / screenshot_filename
    return screenshot_filename, screenshot_path


@pytest.fixture(scope="function")
def output_file(tmp_path):
    tmp_file_full_path = os.path.join(tmp_path, f"file.txt{random.randint(0, 99)}")
    with open(tmp_file_full_path, "w+") as f:
        f.write(f"test data{random.randint(0, 1000)}")
        file_name = tmp_file_full_path.split("/")[-1]
        yield tmp_file_full_path, file_name


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
