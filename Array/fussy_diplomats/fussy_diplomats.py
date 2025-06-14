
# Solution 1: using bit operations
def count_trailing_zeros(x):
    return (x & -x).bit_length() - 1


def total_num_handshakes(delegations: list):
    handshakes = []
    for diplomats in delegations:
        n = len(diplomats)
        diplomats_bytes = diplomats.encode('utf8')
        cnt = 0
        bits_a, bits_b = 0, 0
        for i in range(n):
             bits_a += diplomats_bytes[i] << (8 * i)
             bits_b = (bits_b << 8) + diplomats_bytes[n - 1 - i]
             bits_xor = bits_a ^ bits_b
             zero_cnt = count_trailing_zeros(bits_xor)
             cnt += (zero_cnt // 8) if zero_cnt >= 0 else (i + 1)

        handshakes.append(cnt)
    return handshakes


print(total_num_handshakes(['ababaa', 'ghigh']))



# Solution 2: recursive dp
def find_similar_substrings(s):
    n = len(s)
    i, j = 0, 0

    while i <= j < n and s[i] == s[j]:
        j += 1

    cnt = 0
    repeating_chars = False
    if j > i:
        cnt = (1 + j - i) * (j - i) / 2
        repeating_chars = True

    if repeating_chars:

    while j < n:

        else:



