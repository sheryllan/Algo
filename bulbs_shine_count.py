"""
There are N bulbs, numbered from 1 to N arranged in a row. Bulb number i is wired to bulb number i-1 and first bulb is connected to power socket. Initially all bulbs are OFF and then we turn the bulbs ON according to a given array (explained in following example). A bulb shines if it is ON and all previous bulbs are ON already. We need to find number of moments for which every turned ON bulb shines (Clarification as pointed out in comments by @Prune: Suppose I am turning bulbs ON one by one according to the array given (from left to right), then If I turn a bulb ON and all the previous bulbs are ON then it is shines and this is called a moment. So we need to find total number of such moments when I turn a bulb ON and it shines).

for e.g. Given array [2, 1, 3, 5, 4] we should get answer 3 as follows:

First, we turn bulb 2 ON but bulb 1 is OFF
Then, we turn bulb 1 ON and there is no bulb left to it (So, first moment)
Then, we turn bulb 3 ON and bulbs 1 & 2 are already ON (So, second moment)
Then, we turn bulb 5 On but bulb 4 is OFF
Then, we turn bulb 4 ON and bulbs 1, 2, 3 are already ON (So, third moment)
N is an integer withing range [1, 100000]; All elements of A are distinct; Each element of the given array is an integer in range [1, N]
"""

# O(n log(n)) solution by sorting
def solution(A):
    max_i = 0
    shine_cnt = 0
    for i, bulb in sorted(enumerate(A), key=lambda x: x[1]):
        if i >= max_i:
            shine_cnt += 1
            max_i = i

    return shine_cnt


# assert solution([2, 3, 6, 5, 4, 1]) == 1
# assert solution([2, 3, 4, 1, 5]) == 2
# assert solution([3, 1, 2, 5, 4]) == 3
# assert solution([1, 2, 3, 4]) == 4
# assert solution([3, 2, 1]) == 1
# assert solution([9, 5, 3, 1, 4, 6, 2, 7, 8]) == 4
# assert solution([2, 1, 3, 5, 4]) == 3


# O(n) solution
def solution2(A):
    status = [0] * len(A)
    max_on_bulb = 1
    shine_cnt = 0
    for bulb in A:
        status[bulb - 1] = 1
        if max_on_bulb == bulb:
            shine_cnt += 1
            max_on_bulb += 1
            for i in range(bulb, len(status)):
                if not status[i]:
                    break
                max_on_bulb += 1

    return shine_cnt

assert solution2([2, 3, 6, 5, 4, 1]) == 1
assert solution2([2, 3, 4, 1, 5]) == 2
assert solution2([3, 1, 2, 5, 4]) == 3
assert solution2([1, 2, 3, 4]) == 4
assert solution2([3, 2, 1]) == 1
assert solution2([9, 5, 3, 1, 4, 6, 2, 7, 8]) == 4
assert solution2([2, 1, 3, 5, 4]) == 3


