"""
There are N given points (numbered 0 to N-1) on a plane.
the K-th point is located at coordinates(X[K], Y[K]), and its tag is S[K].
We want to draw a circle centered on coordinates (0,0).
The circle should not contain two points with the same tag.

Write a python function solution(S, X, Y), that, given a string S of length N and 2 arrays X, Y consisting of N integers each,
returns the maximum number of points that lie inside the circle.
The circle may contain only distinct tags.

Points that are on the border of the circle are included within it.
"""


def solution(S, X, Y):
    sq_distances = [x ** 2 + y ** 2 for x, y in zip(X, Y)]
    min_radius = float('inf')
    min_distance_by_tag = {}
    for tag, d in zip(S, sq_distances):
        if tag not in min_distance_by_tag:
            min_distance_by_tag[tag] = (d, float('inf'))
        else:
            min_d, second_min_d = min_distance_by_tag[tag]
            if d < min_d:
                min_d = d
            elif d == min_d or d < second_min_d:
                second_min_d = d

            min_distance_by_tag[tag] = (min_d, second_min_d)
            min_radius = min(min_radius, min_distance_by_tag[tag][1])

    return sum(d < min_radius for d in sq_distances)


assert solution('ABDCA', [-2, -1, -4, -3, 3], [2, -2, 4, 1, -3]) == 3
assert solution('ABAA', [1, 1, -1, -3], [1, 2, 3, -2]) == 2
assert solution('ABA', [2, 1, 2], [2, 2, 2]) == 1
assert solution('ABA', [2, 3, 2], [2, 2, 2]) == 0
