from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем оба числа и вычисляем сумму
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    total = num1 + num2
    print("Сумма:", total)

    # 2. Выбираем значение в выпадающем списке
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(total))  # обязательно str!

    # 3. Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(30)
    if 'browser' in locals():
        browser.quit()
