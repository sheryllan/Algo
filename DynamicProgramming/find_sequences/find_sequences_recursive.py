

def find_sequences(max_seq_len: int = 10, max_vowels: int = 2):
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

    def is_valid(new_key: str, vowel_cnt: int) -> bool:
        return new_key is not None and (new_key not in vowels or vowel_cnt < max_vowels)

    def search(x: int, y: int, seq_len: int, vowel_cnt: int) -> int:
        if seq_len == max_seq_len:
            return 1

        cnt = 0
        for dx, dy in knight_moves:
            x_new, y_new = x+dx, y+dy
            if x_new >= m or y_new >= n or x_new < 0 or y_new < 0:
                continue

            new_key = keypad[x_new][y_new]
            if is_valid(new_key, vowel_cnt):
                new_vowel_cnt = vowel_cnt + int(new_key in vowels)
                cnt += search(x_new, y_new, seq_len + 1, new_vowel_cnt)

        return cnt

    total_cnt = 0
    for i in range(m):
        for j in range(n):
            if keypad[i][j] is None:  # Skip None positions
                continue
            vowel_count = int(keypad[i][j] in vowels)
            total_cnt += search(i, j, 1, vowel_count)

    return total_cnt



if __name__ == '__main__':
    print(find_sequences(10))