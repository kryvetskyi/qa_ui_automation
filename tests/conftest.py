from datetime import datetime
import random
from pathlib import Path

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# def pytest_addoption(parser):
    #parser.addoption("--driver", action="store", default="chrome", help="Enter browser")
    #parser.addoption("--headless", action="store", default="headless", help="Run tests in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    driver = webdriver.Remote(command_executor="http://192.168.0.163:4444/wd/hub", options=options)
    yield driver
    driver.quit()

#@pytest.fixture(scope='function')
#def driver(request):
    # Retrieve the chosen browser from command-line options
 #   browser = request.config.getoption("--driver")

    # Check if only 'chrome' is supported
  #  if browser != 'chrome':
   #     pytest.fail('only chrome is supported at the moment')

    # Retrieve the headless option from command-line options
    #headless = request.config.getoption("--headless")

    # Configure Chrome options
   # options = Options()
    # options.add_argument("--start-maximized")

    # Add headless mode option if requested
    #if headless:
      #  options.add_argument("--headless")

    # Create the Chrome WebDriver instance
    # driver = weibdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    # driver = webdriver.Remote(command_executor="http://3.67.207.173:4444/wd/hub", options=options)
    # yield driver

    # After the test execution, if the test failed, capture and attach a screenshot
    #if request.node.rep_call.failed:
     #   screenshot_filename, screenshot_path = create_screenshot_path()
        #allure.attach(driver.get_screenshot_as_file(screenshot_path),
         #             name=screenshot_filename,
          #            attachment_type=allure.attachment_type.PNG)


def create_screenshot_path():
    # Generate a unique filename and path for the screenshot
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_filename = f"screenshot_{timestamp}.png"
    screenshot_dir = Path(__file__).resolve().parent.parent / 'reports' / 'screenshots'
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    screenshot_path = screenshot_dir / screenshot_filename
    return screenshot_filename, screenshot_path


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


#@pytest.hookimpl(hookwrapper=True, tryfirst=True)
#def pytest_runtest_makereport(item):
    # Yield the test outcome to the hook
 #   outcome = yield
  #  rep = outcome.get_result()

    # Set an attribute on the test item with the test outcome information
    # setattr(item, "rep_" + rep.when, rep)

    # Return the test report outcome
    #return rep
