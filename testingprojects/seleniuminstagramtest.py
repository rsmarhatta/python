from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.google.com')
search_box = driver.find_element(By.CLASS_NAME,"gLFyf")
#print(search_box)
# Enter a search query
driver.implicitly_wait(20)
search_box.send_keys("example12333333333")
searchbutton = driver.find_element(By.XPATH,"descendant::input[@class='gNO89b'][2]")
driver.implicitly_wait(20)
#print("Element is visible? " + str(searchbutton.is_displayed()))
#ActionChains(driver).move_to_element(searchbutton).click(searchbutton).perform()
driver.execute_script("arguments[0].click();", searchbutton)
# Pause the script and wait for user input
input("Press Enter to close the browser...")

# Close the browser
driver.quit()


