def polynomial_differentiator(polynomial: list) -> list:
    """
    Differentiates a given polynomial and returns a list
    :param polynomial: a list where each number represents
    a coefficient of the polynomial
    :return:
    """
    i = -1
    diff_poly = [0] * (len(polynomial) - 1)
    while i > -len(polynomial):
        diff_poly[i] = polynomial[i-1] * (-i)
        i -= 1
    return diff_poly


def newton_raphson(polynomial: list, x0: float, accuracy: int) -> tuple:
    """

    :param polynomial:
    :param x0:
    :param accuracy:
    :return:
    """
    diff_poly = polynomial_differentiator(polynomial)
    for n in range(100*accuracy):

        i = -1
        numerator = 0
        while i >= -len(polynomial):
            numerator += polynomial[i] * (x0 ** (-i - 1))
            i -= 1

        i = -1
        denominator = 0
        while i >= -len(diff_poly):
            denominator += diff_poly[i] * (x0 ** (-i - 1))
            i -= 1

        x_next = x0 - (numerator / denominator)
        tolerance = 10 ** (-accuracy)
        if abs(x_next - x0) < tolerance:
            return round(x_next, accuracy), n
        else:
            x0 = x_next

    else:
        return 0, 0.1
        raise ValueError("Newton-Raphson method has diverged")


def polynomial_solver(polynomial: list, function_range: range, accuracy: int) -> tuple:
    solutions = set()
    for x in function_range:
        solution = newton_raphson(polynomial, x, accuracy)
        if solution[1] != 0.1:
            solutions.add(solution[0])
    solutions_tuple = tuple(solutions)
    return solutions_tuple


p = [1, -21, 175, -735, 1624, -1764, 720]
func_range = range(-1000, 1000, 1)
acc = 2

roots = polynomial_solver(p, func_range, acc)
print(roots)
