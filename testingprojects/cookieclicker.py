from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

service = Service(executable_path="C:/Users/rsmar/.eclipse/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(50)


total_clicked_cookies_id = 'cookies'
product_price_prefix = 'productPrice'
product_prefix = "product"
english_option = WebDriverWait(driver, 30).until(\
        EC.presence_of_element_located((By.ID, 'langSelect-EN')))
english_option = driver.find_element(By.ID, 'langSelect-EN')

english_option.click()


driver.implicitly_wait(50)
cookie = WebDriverWait(driver, 30).until( \
    EC.presence_of_element_located((By.ID, "bigCookie")))
cookie = driver.find_element(By.ID, "bigCookie")
while True:
    try:
        cookies_count = driver.find_element(By.ID,total_clicked_cookies_id).text.split(" ")[0]


        cookie.click()
    except StaleElementReferenceException as e:
        raise e
    for i in range(4):
        WebDriverWait(driver, 30).until( \
            EC.presence_of_element_located((By.ID,product_price_prefix + str(i))))
        product_price = driver.find_element(By.ID,product_price_prefix + str(i)).text.replace(",","")

        if not product_price.isdigit():
            continue
        product_price = int(product_price)
        print(product_price)
        if int(cookies_count) >= product_price:
            # WebDriverWait(driver, 20).until(
            #     EC.element_to_be_clickable((By.ID, product_price_prefix +str(i)))).click()

            # product = driver.find_element(By.ID, product_price_prefix + str(i))
            WebDriverWait(driver, 30).until( \
                EC.element_to_be_clickable((By.ID, product_price_prefix + str(i))))
            product = driver.find_element(By.ID, product_price_prefix + str(i))
            driver.execute_script("arguments[0].scrollIntoView();", product)
            driver.execute_script("arguments[0].click();", product)

            break