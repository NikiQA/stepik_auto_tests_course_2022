
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//*[@name='firstname']").send_keys("Veronika")
    input2 = browser.find_element(By.XPATH, "//*[@name='lastname']").send_keys("Nesterenko")
    input3 = browser.find_element(By.XPATH, "//*[@name='email']").send_keys("test@test.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    
    option1 = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()