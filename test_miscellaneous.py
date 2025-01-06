def test_server_response_time(driver):  # TC007
    import time
    driver.get("https://b2c.passport.rt.ru")
    start_time = time.time()
    driver.find_element(By.ID, "email").send_keys("user@example.com")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "loginButton").click()

    WebDriverWait(driver, 10).until(EC.url_contains("redirect_uri"))
    response_time = time.time() - start_time
    assert response_time <= 5


def test_account_lock_after_three_attempts(driver):  # TC008
    driver.get("https://b2c.passport.rt.ru")
    for _ in range(3):
        driver.find_element(By.ID, "email").send_keys("user@example.com")
        driver.find_element(By.ID, "password").send_keys("wrong_password")
        driver.find_element(By.ID, "loginButton").click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Ваш аккаунт временно заблокирован')]"))
    )
    assert error_message.is_displayed()

def test_password_length_limit(driver):  # TC018
    driver.get("https://b2c.passport.rt.ru/register")
    long_password = "a" * 129
    driver.find_element(By.ID, "password").send_keys(long_password)
    driver.find_element(By.ID, "registerButton").click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Пароль не может быть длиннее 128 символов')]"))
    )
    assert error_message.is_displayed()


def test_authorization_with_social_media(driver):  # TC019
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "socialMediaYandex").click()

    # Проверка перенаправления в окно авторизации Yandex
    WebDriverWait(driver, 10).until(
        EC.url_contains("oauth.yandex.ru")
    )
    assert "oauth.yandex.ru" in driver.current_url


def test_session_timeout(driver):  # TC020
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "email").send_keys("user@example.com")
    driver.find_element(By.ID, "password").send_keys("correct_password")
    driver.find_element(By.ID, "loginButton").click()

    WebDriverWait(driver, 10).until(EC.url_contains("redirect_uri"))
    WebDriverWait(driver, 900).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Сеанс завершён')]"))
    )
    assert "Сеанс завершён" in driver.page_source
