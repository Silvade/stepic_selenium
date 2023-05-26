from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    x = browser.find_element(By.CSS_SELECTOR, '.form-group #input_value').text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, '.form-group #answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
