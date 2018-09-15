def fib_recursive(n):
    # Exponential - T(n - 1) + T(n - 2)

    # Check if Base Case
    if n < 0:
        return False
    if n <= 2:
        return 1
    
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# print(fib_recursive(6))

memoMap = {}

def fib_dynamic(n, memo):
    # Linear Time O(N), Linear Space O(N)

    if n in memo:
        return memo[n]

    if n <= 2:
        return 1
    else:
        fib_number = fib_dynamic(n - 1, memo) + fib_dynamic(n - 2, memo)
        memo[n] = fib_number
        return fib_number

print(fib_dynamic(100, memoMap))

def fib_iterative(n):
    # Linear Time O(N), Constant Space O(1)

    # TODO


