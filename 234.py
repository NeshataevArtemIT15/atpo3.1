import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Нажимаем на кнопку, которая вызывает confirm
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 2. Переключаемся на confirm и принимаем его
    confirm = browser.switch_to.alert
    confirm.accept()

    # 3. На новой странице решаем капчу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # 4. Вводим ответ
    browser.find_element(By.ID, "answer").send_keys(y)

    # 5. Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    if 'browser' in locals():
        browser.quit()
