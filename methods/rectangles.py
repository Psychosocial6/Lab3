def solve(mode, function, a, b, eps):
    n = 4
    sums = []
    while True:
        h = (b - a) / 4
        points = []
        points.append(a)
        for i in range(n - 1):
            points.append(a + h * (i + 1))
        points.append(b)
        int_sum = 0
        if mode == "left":
            for i in range(len(points) - 1):
                int_sum += h * function.f(points[i])
        elif mode == "right":
            for i in range(1, len(points)):
                int_sum += h * function.f(points[i])
        elif mode == "mid":
            for i in range(len(points) - 1):
                int_sum += h * function.f((points[i] + points[i + 1]) / 2)
        if len(sums) > 0:
            if mode == "left" or mode == "right":
                delta = abs(int_sum - sums[-1])
            else:
                delta = abs(int_sum - sums[-1]) / 3
            if delta <= eps:
                return int_sum, n
            else:
                sums.append(int_sum)
                n *= 2
        else:
            sums.append(int_sum)
            n *= 2