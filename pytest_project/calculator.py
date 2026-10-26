class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        """Сложение двух чисел."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """Вычитание."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        """Умножение."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        """Деление с проверкой на ноль."""
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def clear_history(self):
        """Очистка истории."""
        self.history = []
        return True

    def get_history(self):
        """Получить историю операций."""
        return self.history
