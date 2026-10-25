import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Нажимаем на кнопку, которая открывает новую вкладку
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 2. Переключаемся на новую вкладку
    # Получаем список всех открытых вкладок (дескрипторов)
    new_window = browser.window_handles[1]
    # Переключаем управление на вторую вкладку
    browser.switch_to.window(new_window)

    # 3. Решаем капчу на новой странице
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
