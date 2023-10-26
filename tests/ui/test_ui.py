import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.ui
def test_check_incorrect_username():
    # створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # відкриваємо сторінку http://github.com/login
    driver.get("http://github.com/login")

    # закриваємо браузер
    driver.close()