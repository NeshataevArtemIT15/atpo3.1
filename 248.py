import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Явное ожидание: ждём, пока в элементе с id="price" появится текст "$100"
    # Таймаут 12 секунд (по условию — не меньше 12)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 2. Нажимаем кнопку "Book"
    browser.find_element(By.ID, "book").click()

    # 3. Решаем математическую задачу на новой странице
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # 4. Вводим ответ
    browser.find_element(By.ID, "answer").send_keys(y)

    # 5. Нажимаем кнопку "Solve"
    browser.find_element(By.ID, "solve").click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    if 'browser' in locals():
        browser.quit()
