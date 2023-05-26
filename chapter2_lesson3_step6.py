from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    newWindowName = browser.window_handles[1]
    browser.switch_to.window(newWindowName)

    x = browser.find_element(By.CSS_SELECTOR, '.form-group #input_value').text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, '.form-group #answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
