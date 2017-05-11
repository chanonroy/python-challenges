"""
A zero-indexed array A consisting of N integers is given.
An equilibrium index of this array is any integer P such that 0 ≤ P < N and the
sum of elements of lower indices is equal to the sum of elements of higher indices, i.e.
"""

def solution(A):
    # Best case can be O(n)

    left_sum = 0
    total_sum = 0

    for i in A:
        total_sum += i

    for index, value in enumerate(A):

        total_sum -= value

        if left_sum == total_sum:
            return index

        left_sum += value

    return -1
