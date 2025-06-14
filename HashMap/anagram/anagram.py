from collections import Counter


def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)


assert are_anagrams('below', 'elbow') is True
assert are_anagrams('beat', 'boat') is False
assert are_anagrams('why', 'heyy') is False


def distance_anagrams(s1, s2):
    counter1 = Counter(s1)
    counter2 = Counter(s2)

    # Take into account if the lengths do not match
    longer, shorter = counter1, counter2
    if len(s2) > len(s1):
        longer, shorter = counter2, counter1
    dist = sum((longer - shorter).values())
    return dist


assert distance_anagrams('cast', 'catt') == 1
assert distance_anagrams('cat', 'xyz') == 3
assert distance_anagrams('hello', 'okklll') == 3