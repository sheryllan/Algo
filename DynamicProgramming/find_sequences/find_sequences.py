

def find_sequences(max_seq_len: int = 10, max_vowels: int = 2) -> int:
    keypad = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'J'],
        ['K', 'L', 'M', 'N', 'O'],
        [None, '1', '2', '3', None]
    ]
    vowels = {'A', 'E', 'I', 'O'}
    knight_moves = [
        (-2, -1), (-2, 1),
        (2, -1), (2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2)
    ]
    m = len(keypad)
    n = len(keypad[0])

    # stores the count for a sequence of certain length whose last key is at position (i,j) with vowel count ranging from 0 to 2
    states = {}
    graph = {}  # stores the key positions going from a given key with a knight move
    for i in range(m):
        for j in range(n):
            if keypad[i][j] is None:
                continue

            # at a given position (i, j), the state value should be a matrix of max_seq_len * (max_vowels + 1)
            # but because current move is only dependent on last move, only 2 states of sequence length is needed
            states[(i, j)] = [[0] * (max_vowels + 1) for _ in range(2)]
            vowel_cnt = int(keypad[i][j] in vowels)
            states[(i, j)][0][vowel_cnt] = 1  # the initial count set to 1 for sequence of 1 key

            graph[(i, j)] = []
            for dx, dy in knight_moves:
                i_new, j_new = i + dx, j + dy
                if i_new >= m or j_new >= n or i_new < 0 or j_new < 0:
                    continue

                if keypad[i_new][j_new] is None:
                    continue

                graph[(i, j)].append((i_new, j_new))

    # traverse through each sequence length, and each key, and for each possible vowel count,
    # sum up the counts from the recorded states of all possible knight moves with - 1 sequence length
    for k in range(1, max_seq_len):
        for i, j in graph:
            vowel_increment = int(keypad[i][j] in vowels)
            for vowel_cnt in range(vowel_increment, max_vowels + 1):
                cnt = 0
                for i_prev, j_prev in graph[(i, j)]:
                    prev_seq_id = (k-1) % 2
                    prev_vowel_cnt = vowel_cnt - vowel_increment
                    cnt += states[(i_prev, j_prev)][prev_seq_id][prev_vowel_cnt]

                states[(i, j)][k % 2][vowel_cnt] = cnt

    # the total count is the sum of all states at the max sequence length
    return sum(sum(states[pos][(max_seq_len-1) % 2]) for pos in states)


if __name__ == '__main__':
    print(find_sequences(10, 2))