import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser......")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser......")
    else:
        driver = webdriver.Edge()
        print("Launching Edge browser........")

    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture()
def browser(request):
    return request.config.getoption("browser")

"""def pytest_configure(config):
    metadata['Project Name'] = 'Automation Test Store'
    metadata['Module Name'] = 'Authentication'
    config._metadata['Tester Name'] = 'Swetha'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)"""


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata['Project Name'] = 'Automation Test Store'
    metadata['Module Name'] = 'Authentication'
    metadata['Tester Name'] = 'Swetha'
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
