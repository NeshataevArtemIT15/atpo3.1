import time
from selenium.webdriver.common.by import By

def test_add_to_basket_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Обязательная пауза для визуальной проверки языка (по условию задания)
    time.sleep(30)
    
    # Ищем кнопку добавления в корзину по уникальному CSS-селектору
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    
    # Проверяем, что кнопка отображается на странице
    assert button.is_displayed(), "Кнопка добавления в корзину не найдена на странице!"
