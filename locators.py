from selenium.webdriver.common.by import By


class RegisterPageLocators:
# Локаторы страницы регистрации (/register)

    REGISTRATION_TITLE = (By.XPATH, "//h2[text()='Регистрация']") # заголовок страницы «Регистрация»
    REGISTER_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input") # поле ввода имени
    REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input") # поле ввода Email
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']") # поле ввода пароля
    PASSWORD_ERROR = (By. CLASS_NAME, "input__error") # текст ошибки при некорректном пароле (слишком короткий)
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # кнопка «Зарегистрироваться»
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")  # ссылка «Войти» в аккаунт внизу формы регистрации


class LoginPageLocators:
# Локаторы страницы входа в аккаунт (/login)
    
    PAGE_TITLE = (By.XPATH, "//h2[text()='Вход']")  # Заголовок страницы «Вход»
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")  # Поле ввода Email
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль']")  # Поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка «Войти»
    REGISTER_LINK = (By.CSS_SELECTOR, "a[href='/register']") # ссылка "Зарегистрироваться"
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/forgot-password']")  # ссылка "Восстановить пароль"
    ACCOUNT_LINK_IN_FORGOT_PASSWORD = (By.CSS_SELECTOR, "a[href='/login']") # ссылка на вход в аккаунт в форме восстановления пароля (/forgot-password)

class PersonalAccountLocators:
# Локаторы страницы личного кабинета (/profile)

    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # кнопка «Выход» из Личного кабинета
    ACCOUNT_LINK_TO_PROFILE = (By.CSS_SELECTOR, "a[href='/account']") # переход по ссылке в Личный кабинет

class MainPageLocators:
# Локаторы главной страницы (конструктор бургеров)

    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка «Войти в аккаунт» на главной странице
    ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href='/account']") # ссылка на аккаунт "Личный Кабинет" на главной странице

    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']") # переход из Личного кабинета в Конструктор
    LOGO = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2 a") # LOGO

    BUN_TAB = (By.XPATH, "//span[text()='Булки']")  # Таб-заголовок раздела «Булки» (локатор для клика)
    SAUCE_TAB = (By.XPATH, "//span[text()='Соусы']")  # Таб-заголовок раздела «Соусы» (локатор для клика)
    FILLING_TAB = (By.XPATH, "//span[text()='Начинки']")  # Таб-заголовок раздела «Начинки» (локатор для клика)
    BUN_SECTION = (By.XPATH, "//span[text()='Булки']/..")  # Контейнер раздела «Булки»
    SAUCE_SECTION = (By.XPATH, "//span[text()='Соусы']/..")  # Контейнер раздела «Соусы»
    FILLING_SECTION = (By.XPATH, "//span[text()='Начинки']/..")  # Контейнер раздела «Начинки»
