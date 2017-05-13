# Maximum sum subarray problem
# Kadane's Algorithm O(n)

# test1 = [-1, -2, 3, 4, -5, 6]
test2 = [-2, 3, 2, -1]  # 5


def kadane(array):
    """ Use what you've seen so far """

    # sum of maximum array at current index
    max_current = 0
    # highest sum we've seen so far
    max_global = 0

    for i in range(0, len(array) - 1):

        # either current or current combined with previous max sum
        max_current = max(array[i], max_current + array[i])
        if max_current > max_global:
            max_global = max_current

    return max_global


print(kadane(test2))
