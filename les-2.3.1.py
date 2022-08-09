from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math


try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    option1 = browser.find_element(By.XPATH,"//*[@class='btn btn-primary']").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    browser.switch_to.window(browser.window_handles[0])
    def calc(x):   return str(math.log(abs(12*math.sin(int(x)))))
    print(calc(916))
    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    print(x) 
    
    input1 = browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)
    time.sleep(1)
    option2 = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
    time.sleep(1)
    alert = browser.switch_to.alert
    alert.accept()
    print(browser.switch_to.alert.text)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()