import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # Добавляем параметр --language в командную строку, по умолчанию английский
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, es, fr, etc.")


@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение языка из командной строки
    user_language = request.config.getoption("language")
    
    # Настраиваем опции Chrome
    options = Options()
    # Устанавливаем язык браузера через настройки (самый надежный способ)
    options.add_experimental_option('prefs', {
        'intl.accept_languages': user_language
    })
    
    print(f"\nЗапускаем браузер с языком: {user_language}")
    browser = webdriver.Chrome(options=options)
    
    yield browser
    browser.quit()
