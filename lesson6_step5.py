from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Вычисляем текст ссылки, по которой нужно кликнуть
    link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    print("Ищем ссылку с текстом:", link_text)

    # Находим и кликаем по ссылке
    link = browser.find_element(By.LINK_TEXT, link_text)
    link.click()

    # Заполняем форму
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    if 'browser' in locals():
        browser.quit()
