from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.NAME, "firstname")
    first.send_keys("Ivan")
    second = browser.find_element(By.NAME, "lastname")
    second.send_keys("Ivanov")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("email")

    file = browser.find_element(By.NAME, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'code.txt')
    file.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
