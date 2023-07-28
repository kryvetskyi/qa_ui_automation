import random
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    driver = webdriver.Remote(command_executor="http://192.168.0.164:4444/wd/hub", options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def output_file(tmp_path):
    # Create the full path of the temporary file
    tmp_file_full_path = tmp_path / f"file.txt{random.randint(0, 99)}"

    # Write test data to the temporary file
    with open(tmp_file_full_path, "w+") as f:
        test_data = f"test data{random.randint(0, 1000)}"
        f.write(test_data)

        # Extract the file name from the full path
        file_name = tmp_file_full_path.name

        # Yield the full path and file name to the test
        yield tmp_file_full_path, file_name
