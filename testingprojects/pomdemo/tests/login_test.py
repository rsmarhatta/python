from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import pytest
import time
from pomdemo.pages.login_page import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # Yield the WebDriver instance
    yield driver
    # Close the WebDriver instance
    driver.quit()


def test_login(driver):
    login_first = LoginPage(driver)
    login_first.open_page("https://trytestingthis.netlify.app/")
    time.sleep(5)
    login_first.enter_username("test")
    login_first.enter_password("test")
    time.sleep(5)
    login_first.click_login()
    time.sleep(5)
    # username_input = driver.find_element(By.ID, "uname")
    # password_input = driver.find_element(By.ID, "pwd")
    # login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    #
    # username_input.send_keys(username)
    # password_input.send_keys(password)
    # login_button.click()
    # time.sleep(5)
    # assert "Successful" in driver.page_source
