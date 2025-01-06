import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_authorization_with_valid_data(driver):  # TC001
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "email").send_keys("valid_user@example.com")
    driver.find_element(By.ID, "password").send_keys("correct_password")
    driver.find_element(By.ID, "loginButton").click()

    WebDriverWait(driver, 10).until(EC.url_contains("redirect_uri"))
    assert "redirect_uri" in driver.current_url


def test_authorization_with_invalid_email(driver):  # TC002
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "email").send_keys("invalid-email")
    driver.find_element(By.ID, "password").send_keys("anyPassword123")
    driver.find_element(By.ID, "loginButton").click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Введите корректный email')]"))
    )
    assert error_message.is_displayed()


def test_password_recovery_by_email(driver):  # TC003
    driver.get("https://b2c.passport.rt.ru/forgot-password")
    driver.find_element(By.ID, "email").send_keys("registered_user@example.com")
    driver.find_element(By.ID, "getCodeButton").click()

    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Пароль успешно изменён')]"))
    )
    assert success_message.is_displayed()


def test_tab_switch_on_phone_input(driver):  # TC004
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "phone").send_keys("+79876543210")

    active_tab = driver.find_element(By.CSS_SELECTOR, ".tab.active")
    assert active_tab.text == "Номер"

def test_tab_switch_on_email_input(driver):  # TC009
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "email").send_keys("user@example.com")

    active_tab = driver.find_element(By.CSS_SELECTOR, ".tab.active")
    assert active_tab.text == "Почта"


def test_feedback_form_submission(driver):  # TC010
    driver.get("https://b2c.passport.rt.ru/feedback")
    driver.find_element(By.ID, "name").send_keys("Иван Иванов")
    driver.find_element(By.ID, "email").send_keys("user@example.com")
    driver.find_element(By.ID, "message").send_keys("Тестовое сообщение.")
    driver.find_element(By.ID, "submitButton").click()

    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Ваш запрос отправлен')]"))
    )
    assert success_message.is_displayed()


def test_login_with_phone(driver):  # TC011
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "phone").send_keys("+79876543210")
    driver.find_element(By.ID, "password").send_keys("correct_password")
    driver.find_element(By.ID, "loginButton").click()

    WebDriverWait(driver, 10).until(EC.url_contains("redirect_uri"))
    assert "redirect_uri" in driver.current_url


def test_login_with_incorrect_password(driver):  # TC012
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "phone").send_keys("+79876543210")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "loginButton").click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Неверный логин или пароль')]"))
    )
    forgot_password_element = driver.find_element(By.ID, "forgotPassword")
    assert error_message.is_displayed()
    assert forgot_password_element.value_of_css_property("color") == "rgb(255, 165, 0)"


def test_logout_functionality(driver):  # TC013
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "email").send_keys("user@example.com")
    driver.find_element(By.ID, "password").send_keys("correct_password")
    driver.find_element(By.ID, "loginButton").click()

    WebDriverWait(driver, 10).until(EC.url_contains("redirect_uri"))
    driver.find_element(By.ID, "logoutButton").click()

    WebDriverWait(driver, 10).until(EC.url_contains("b2c.passport.rt.ru"))
    assert "b2c.passport.rt.ru" in driver.current_url
