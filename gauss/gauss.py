import numpy as np

def gauss_with_pivoting(A, b):
    """
    Решение системы линейных уравнений методом Гаусса с выбором главного элемента.

    Вход:
    A -- квадратная матрица коэффициентов (numpy.ndarray)
    b -- вектор свободных членов (numpy.ndarray)

    Выход:
    x -- вектор решения системы (numpy.ndarray)
    """
    A = A.astype(float)  # Преобразуем к float для точности вычислений
    b = b.astype(float)
    n = len(b)

    # Прямой ход
    for k in range(n - 1):
        # Поиск главного элемента в столбце k (по модулю)
        max_row = np.argmax(np.abs(A[k:, k])) + k

        # Перестановка строк, если нужно
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[[k, max_row]] = b[[max_row, k]]

        # Исключение переменной k из уравнений ниже
        for i in range(k + 1, n):
            if A[k, k] == 0:
                raise ValueError("Нулевой главный элемент, система не решается методом Гаусса с выбором главного элемента.")
            factor = A[i, k] / A[k, k]
            A[i, k:] = A[i, k:] - factor * A[k, k:]
            b[i] = b[i] - factor * b[k]

    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if A[i, i] == 0:
            raise ValueError("Система несовместна или имеет бесконечное множество решений.")
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x

# Пример использования
if __name__ == "__main__":
    A = np.array([[2, -1, 1],
                  [3, 3, 9],
                  [3, 3, 5]], dtype=float)
    b = np.array([2, -1, 4], dtype=float)

    solution = gauss_with_pivoting(A, b)
    print("Решение системы:", solution)
