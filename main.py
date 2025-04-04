def is_long(password):
    return len(password) > 12


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_upper(password):
    return any(char.isupper() for char in password)


def has_lower(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(not char.isalnum() for char in password)


def rating_password(password):
    checks = [
        is_long,
        has_digit,
        has_upper,
        has_lower,
        has_symbols
    ]
    return sum(2 for func in checks if func(password))


def main():
    password = input("Введите пароль: ")
    score = rating_password(password)
    print(f"Рейтинг: {score} балла")


if __name__ == "__main__":
    main()
