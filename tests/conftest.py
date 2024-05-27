import pytest
from selenium import webdriver
import os


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    take_screenshot = request.config.getoption("--screenshot")
    print(f"creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome()
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox' but got {browser}")
    # Maximize the window
    my_driver.maximize_window()
    yield my_driver
    if request.node.rep_call.failed and take_screenshot:
        # Take screenshot on test failure
        screenshot_name = f"{request.node.nodeid.replace('::', '_')}.png"
        my_driver.save_screenshot(screenshot_name)
        print(f"Screenshot taken: {screenshot_name}")
    print(f"closing {browser} driver")
    my_driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Set an attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to execute tests(chrome or firefox")
    parser.addoption("--screenshot", action="store_true", help="take screenshots on test failure")
