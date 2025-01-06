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

def test_registration_with_existing_email(driver):  # TC014
    driver.get("https://b2c.passport.rt.ru/register")
    driver.find_element(By.ID, "email").send_keys("existing_user@example.com")
    driver.find_element(By.ID, "password").send_keys("StrongPass123!")
    driver.find_element(By.ID, "registerButton").click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Этот email уже используется')]"))
    )
    assert error_message.is_displayed()


def test_phone_validation(driver):  # TC015
    driver.get("https://b2c.passport.rt.ru/register")
    driver.find_element(By.ID, "phone").send_keys("123")
    driver.find_element(By.ID, "registerButton").click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Введите корректный номер телефона')]"))
    )
    assert error_message.is_displayed()


def test_authorization_with_temporary_code(driver):  # TC016
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "temporaryCodeTab").click()
    driver.find_element(By.ID, "phone").send_keys("+79876543210")
    driver.find_element(By.ID, "sendCodeButton").click()

    # Эмуляция отправленного временного кода
    driver.find_element(By.ID, "temporaryCode").send_keys("123456")
    driver.find_element(By.ID, "loginButton").click()

    WebDriverWait(driver, 10).until(EC.url_contains("redirect_uri"))
    assert "redirect_uri" in driver.current_url


def test_expired_temporary_code(driver):  # TC017
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "temporaryCodeTab").click()
    driver.find_element(By.ID, "phone").send_keys("+79876543210")
    driver.find_element(By.ID, "sendCodeButton").click()

    # Ожидание истечения времени действия кода
    WebDriverWait(driver, 61).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Код истёк, запросите новый')]"))
    )
    assert "Код истёк, запросите новый" in driver.page_source
