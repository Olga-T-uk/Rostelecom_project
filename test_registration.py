def test_registration_with_unique_data(driver):  # TC005
    driver.get("https://b2c.passport.rt.ru/register")
    driver.find_element(By.ID, "firstName").send_keys("Иван")
    driver.find_element(By.ID, "lastName").send_keys("Иванов")
    driver.find_element(By.ID, "email").send_keys("new_user@example.com")
    driver.find_element(By.ID, "password").send_keys("StrongPass123!")
    driver.find_element(By.ID, "confirmPassword").send_keys("StrongPass123!")
    driver.find_element(By.ID, "registerButton").click()

    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Регистрация успешна')]"))
    )
    assert success_message.is_displayed()


def test_registration_with_short_password(driver):  # TC006
    driver.get("https://b2c.passport.rt.ru/register")
    driver.find_element(By.ID, "password").send_keys("12345")
    driver.find_element(By.ID, "registerButton").click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Пароль должен содержать не менее 8 символов')]"))
    )
    assert error_message.is_displayed()
