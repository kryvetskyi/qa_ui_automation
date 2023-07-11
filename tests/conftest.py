import os
import random

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

    if headless:
        options.add_argument(headless)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def output_file(tmp_path):
    tmp_file_full_path = os.path.join(tmp_path, f"file.txt{random.randint(0, 99)}")
    with open(tmp_file_full_path, "w+") as f:
        f.write(f"test data{random.randint(0, 1000)}")
        file_name = tmp_file_full_path.split("/")[-1]
        yield tmp_file_full_path, file_name
