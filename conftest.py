import os
import random

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture(scope='function')
# def driver():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     yield driver
#     driver.quit()


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    options = webdriver.ChromeOptions()
    options.set_capability("browser", "chrome")

    driver = webdriver.Remote(command_executor="http://localhost:4444", options=options)
    yield driver


@pytest.fixture(scope="function")
def output_file(tmp_path):
    tmp_file_full_path = os.path.join(tmp_path, f"file.txt{random.randint(0, 99)}")
    with open(tmp_file_full_path, "w+") as f:
        f.write(f"test data{random.randint(0, 1000)}")
        file_name = tmp_file_full_path.split("/")[-1]
        yield tmp_file_full_path, file_name

