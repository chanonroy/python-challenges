'''
https://www.hackerrank.com/challenges/ctci-array-left-rotation
Given an array of integers and a number perform left rotations on the array.
'''


def array_left_rotation(a, n, k):
    # array, num of ints, num of rotations

    rotations = k
    holder = []

    # remove first index and put into holder
    while rotations > 0:
        holder.append(a[0])
        a.pop(0)
        rotations -= 1

    # concatenate arrays
    return a + holder


def array_left_rotation_two(arr, total, rotations):
    # another version of the problem above

    old = arr[rotations:total]
    del arr[rotations:total]
    print(old + arr)


array_left_rotation_two([1, 2, 3, 4, 5], 5, 4)
