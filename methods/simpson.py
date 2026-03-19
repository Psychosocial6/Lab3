def solve(function, a, b, eps):
    n = 4
    sums = []
    while True:
        h = (b - a) / n
        points = [a]
        for i in range(n - 1):
            points.append(a + (i + 1) * h)
        points.append(b)
        int_sum = function.f(points[0]) + function.f(points[-1])
        for i in range(1, len(points) - 1):
            if i % 2 != 0:
                int_sum += 4 * function.f(points[i])
            else:
                int_sum += 2 * function.f(points[i])
        int_sum *= h / 3
        if len(sums) > 0:
            delta = abs(int_sum - sums[-1]) / 15
            if delta <= eps:
                return int_sum, n
            else:
                n *= 2
                sums.append(int_sum)
        else:
            sums.append(int_sum)
            n *= 2
