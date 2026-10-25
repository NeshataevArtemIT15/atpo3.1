import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Заполняем текстовые поля
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("test@test.com")

    # 2. Загружаем файл
    # Определяем папку, в которой находится сам скрипт
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Собираем полный путь к файлу file.txt
    file_path = os.path.join(current_dir, "file.txt")
    print("Путь к файлу:", file_path)

    # Находим поле для загрузки файла и отправляем в него путь
    browser.find_element(By.ID, "file").send_keys(file_path)

    # 3. Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    if 'browser' in locals():
        browser.quit()
