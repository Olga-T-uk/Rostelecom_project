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
