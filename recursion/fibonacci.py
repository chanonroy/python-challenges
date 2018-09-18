def fib_recursive(n):
    # Exponential - T(n - 1) + T(n - 2)

    # Check if Base Case
    if n <= 2:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)

# print(fib_recursive(6))

memoMap = {}

def fib_dynamic(n, memo):
    # Linear Time O(N), Linear Space O(N)

    # Check Cache
    if n in memo:
        return memo[n]

    # Check Base Case
    if n <= 2:
        return 1
    else:
        fib_number = fib_dynamic(n - 1, memo) + fib_dynamic(n - 2, memo)
        memo[n] = fib_number
        return fib_number

# print(fib_dynamic(100, memoMap))


def fib_bottom_up(n):
    # Linear Time O(N), Constant Space O(1)

    if n == 0 or n == 1:
        return n

    twoBehind = 0
    oneBehind = 1
    fib = 0

    for i in range(1, n + 1):
        fib = oneBehind + twoBehind
        twoBehind = oneBehind
        oneBehind = fib

    return fib


result = fib_bottom_up(1000)
print(result)
