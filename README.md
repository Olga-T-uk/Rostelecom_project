# Описание
Этот проект содержит 20 автоматизированных тестов для проверки функциональности сайта Ростелеком.

Тесты реализованы на Python с использованием фреймворка PyTest и библиотеки Selenium WebDriver.

Проверяемые сценарии
Авторизация с корректными данными — проверяет успешный вход в систему.
Авторизация с некорректным email — проверяет вывод ошибки при неверном формате email.
Восстановление пароля по email — тестирует процесс восстановления пароля.
Автоматический выбор таба при вводе номера телефона.
Регистрация с уникальными данными — проверяет успешную регистрацию нового пользователя.
Ввод пароля менее 8 символов — проверяет валидацию минимальной длины пароля.
Максимальное время ожидания авторизации.
Блокировка аккаунта после 3 неверных попыток ввода пароля.
Автоматический выбор таба при вводе email.
Проверка формы обратной связи.
Авторизация по номеру телефона — с корректными данными.
Авторизация по номеру телефона — с некорректным паролем.
Проверка кнопки "Выйти".
Регистрация с уже существующим email.
Валидация телефона — проверка при вводе некорректного номера.
Авторизация по временному коду.
Вход с истёкшим временным кодом.
Проверка ограничения длины пароля.
Авторизация через социальные сети.
Автоматическое завершение сеанса.
Установка и запуск

#Предварительные требования
Установите Python 3.
Убедитесь, что установлен браузер (например, Google Chrome) и соответствующий драйвер (например, chromedriver) находится в PATH.


rostelecom-tests/
│
├── tests/
│   ├── test_authorization.py  # Тесты на авторизацию
│   ├── test_registration.py   # Тесты на регистрацию
│   ├── test_miscellaneous.py  # Прочие тесты
│
├── conftest.py                # Фикстуры PyTest
├── README.md                  # Описание проекта    


Запустить  файл test_authorization.py 

pytest tests/test_authorization.py

Запустить  файл    registration.py   

pytest tests/test_registration.py    

Запустите все тесты:    

pytest tests/
