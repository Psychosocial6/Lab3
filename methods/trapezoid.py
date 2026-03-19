def solve(function, a, b, eps):
    n = 4
    sums = []
    while True:
        h = (b - a) / n
        points = [a]
        for i in range(n - 1):
            points.append(a + (i + 1) * h)
        points.append(b)
        int_sum = 0
        for i in range(n):
            y1 = function.f(points[i])
            y2 = function.f(points[i + 1])
            int_sum += (y1 + y2) / 2 * h
        if len(sums) > 0:
            delta = abs(int_sum - sums[-1]) / 3
            if delta <= eps:
                return int_sum, n
            else:
                n *= 2
                sums.append(int_sum)
        else:
            sums.append(int_sum)
            n *= 2