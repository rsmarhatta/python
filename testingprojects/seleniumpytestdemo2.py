from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # Yield the WebDriver instance
    yield driver
    # Close the WebDriver instance
    driver.quit()


@pytest.mark.parametrize("username,password", [
    ("test", "test"),
    ("Test2", "password2"),
    ("user12", "password1"),
    ("user23", "password2"),

])
def test_login(driver,username,password):
    driver.get("https://trytestingthis.netlify.app/")
    time.sleep(5)
    username_input = driver.find_element(By.ID, "uname")
    password_input = driver.find_element(By.ID, "pwd")
    login_button = driver.find_element(By.XPATH, "//input[@type='submit']")

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()
    time.sleep(5)
    assert "Successful" in driver.page_source
