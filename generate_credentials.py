import random
import string


def generate_email(first_name = 'User', last_name = 'Test', cohort_number = 55):
    random_digits = str(random.randint(100, 999))
    return f"{first_name}{last_name}{cohort_number}{random_digits}@ya.ru"

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))