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
    yield driver

    driver.close()
    driver.quit()

def test_google_search(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.ID,"APjFqb")
    search_box.send_keys("hello world!")
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)
    print("DONE")

