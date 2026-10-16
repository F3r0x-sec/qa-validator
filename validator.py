def get_input(prompt: str) -> str:
    """Безопасно получает строку от пользователя, убирает пробелы по краям."""
    try:
        value = input(prompt)
    except (EOFError, KeyboardInterrupt):
        return ""
    return value.strip()


def validate_email(email: str) -> tuple[bool, str]:
    """Проверяет формат email."""
    if not email:
        return False, "поле пустое"
    if "@" not in email or "." not in email.split("@")[-1]:
        return False, "неверный формат email (нужно имя@домен.зона)"
    if email.startswith("@") or email.endswith("."):
        return False, "email не может начинаться с @ или заканчиваться точкой"
    return True, "ok"


def validate_password(password: str) -> tuple[bool, str]:
    """Проверяет пароль: минимум 8 символов и хотя бы одна цифра."""
    if not password:
        return False, "поле пустое"
    if len(password) < 8:
        return False, f"слишком короткий (нужно 8, введено {len(password)})"
    if not any(ch.isdigit() for ch in password):
        return False, "нет ни одной цифры"
    return True, "ok"


def validate_age(age: str) -> tuple[bool, str]:
    """Проверяет возраст: число от 18 до 99."""
    if not age:
        return False, "поле пустое"
    if not age.isdigit():
        return False, "не число"
    number = int(age)
    if not (18 <= number <= 99):
        return False, f"вне диапазона 18–99 (введено {number})"
    return True, "ok"


def build_report(results: dict) -> str:
    """Собирает текстовый отчёт по результатам проверок."""
    lines = ["", "===== ОТЧЁТ ПРОВЕРКИ ====="]
    all_ok = True
    for field, (ok, reason) in results.items():
        mark = "PASS" if ok else "FAIL"
        lines.append(f"[{mark}] {field}: {reason}")
        if not ok:
            all_ok = False
    lines.append("==========================")
    lines.append("Итог: данные корректны" if all_ok else "Итог: есть ошибки")
    return "\n".join(lines)


def main() -> None:
    """Точка входа: собирает ввод и печатает отчёт."""
    print("Проверка тестовых данных QA-инженера")

    email = get_input("Введите email: ")
    password = get_input("Введите пароль: ")
    age = get_input("Введите возраст: ")

    results = {
        "email": validate_email(email),
        "пароль": validate_password(password),
        "возраст": validate_age(age),
    }

    print(build_report(results))


if __name__ == "__main__":
    main()