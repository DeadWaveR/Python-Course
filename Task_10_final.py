from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://google.com/ncr")

search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("selenide")
search_input.send_keys(Keys.RETURN)

first_result = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.g"))
)
first_result_link = first_result.find_element(By.TAG_NAME, "a")
assert "selenide.org" in first_result_link.get_attribute("href")

images_link = driver.find_element(By.LINK_TEXT, "Картинки")
images_link.click()

first_image = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.isv-r a"))
)
assert "selenide.org" in first_image.get_attribute("href")


all_link = driver.find_element(By.LINK_TEXT, "Все")
all_link.click()


first_result_after_back = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.g"))
)
first_result_link_after_back = first_result_after_back.find_element(By.TAG_NAME, "a")
assert "selenide.org" in first_result_link_after_back.get_attribute("href")

driver.quit()