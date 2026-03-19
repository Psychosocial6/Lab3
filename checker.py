from methods import trapezoid

def check(function, a, b):
    s = function.s
    if s is None or s < a or s > b:
        return True
    eps = 10 ** -4
    min_delta = 10 ** -3
    max_iter = 20
    ratio = 0.5
    prev_I = None
    for i in range(max_iter):
        current_I = 0.0
        try:
            if s > a:
                d_left = (s - a) * ratio
                current_I += trapezoid.solve(function, a, s - d_left, eps)
            if s < b:
                d_right = (b - s) * ratio
                current_I += trapezoid.solve(function, s + d_right, b, eps)
        except Exception:
            return False
        if prev_I is not None:
            diff = abs(current_I - prev_I)
            if diff < min_delta:
                return True
            if abs(current_I) > 10 ** 7 or diff > 10 ** 7:
                return False
        prev_I = current_I
        ratio /= 2.0
    return False
