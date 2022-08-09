from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = " http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

   
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x) 

    input1 = browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)

    option1 = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
    option2 = browser.find_element(By.XPATH, "//input[@id='robotsRule']").click()
    option3 = browser.find_element(By.XPATH, "//button[@class='btn btn-default']").click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()