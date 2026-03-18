from function import Function

functions = {
    1: Function(
        function_string="-x^3 - x^2 - 2x + 1",
        function=lambda x: -1 * x ** 3 - x ** 2 - 2 * x + 1
    ),
    2: Function(
        function_string="-3x^3 - 5x^2 + 4x - 2",
        function=lambda x: -3 * x ** 3 - 5 * x ** 2 + 4 * x - 2
    ),
    3: Function(
        function_string="-x^3 - x^2 + x + 3",
        function=lambda x: -1 * x ** 3 - x ** 2 + x + 3
    )
}