# Константы проекта: базовый URL и эндпоинты.
BASE_URL = "https://stellarburgers.education-services.ru"

# Эндпоинты
LOGIN_ENDPOINT = "/login"
REGISTER_ENDPOINT = "/register"
FORGOT_PASSWORD_ENDPOINT = "/forgot-password"
ACCOUNT_PROFILE_ENDPOINT = "/account/profile"

# Полные URL
LOGIN_URL = f"{BASE_URL}{LOGIN_ENDPOINT}"
REGISTER_URL = f"{BASE_URL}{REGISTER_ENDPOINT}"
FORGOT_PASSWORD_URL = f"{BASE_URL}{FORGOT_PASSWORD_ENDPOINT}"
ACCOUNT_PROFILE_URL = f"{BASE_URL}{ACCOUNT_PROFILE_ENDPOINT}"