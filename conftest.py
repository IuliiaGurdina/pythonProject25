import pytest
from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# @pytest.fixture
# def auth_key() -> json:
#     status, result = pf.get_api_key(email=valid_email, password=valid_password)
#     assert status == 200
#     assert 'key' in result
#     return result


@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome()

   # Переходим на страницу авторизации
   driver.get('https://petfriends.skillfactory.ru/login')

   driver.maximize_window()
   yield driver

   driver.quit()

@pytest.fixture()
def my_pets(driver):
    driver.find_element(By.ID, 'email').send_keys(valid_email)
# Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys(valid_password)
# Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
# Ждем когда окажемся на главной странице пользователя
    WebDriverWait(driver, 11).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), 'PetFriends'))
    driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()

