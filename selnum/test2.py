from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get("https://books.toscrape.com/?")

driver.implicitly_wait(0.5)
botto = driver.find_element(
    by=By.CSS_SELECTOR,
    value="#default > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child(1) > article > div.product_price > form > button",
)
botto.click()

html_elem = driver.find_element(by=By.TAG_NAME, value="html")
html_elem.send_keys(Keys.END)
html_elem.send_keys(Keys.HOME)


driver.close()
