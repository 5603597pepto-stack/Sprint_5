import random
import string

# генерация логина
def generate_email(first_name = 'User', last_name = 'Test', cohort_number = 55):
    random_digits = str(random.randint(100, 999))
    return f"{first_name}{last_name}{cohort_number}{random_digits}@ya.ru"

# генерация пароля
def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# формирование данных пользователя
def get_user_data():
    return {
        "name": "Анна",
        "email": generate_email(),
        "password": generate_password(),
    }
