from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Edge()

driver.get("https://www.baidu.com/")

# title = driver.title

driver.implicitly_wait(0.5)

# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# submit_button.click()

# message = driver.find_element(by=By.ID, value="message")
# text = message.text

# <input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
inpyt_box = driver.find_element(by=By.ID, value="kw")
sub_botton = driver.find_element(by=By.ID, value="su")
inpyt_box.send_keys("python")
sub_botton.click()

driver.quit()
