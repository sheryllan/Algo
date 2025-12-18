def build_keypad():
    """Build the keypad as a 2D grid with coordinates."""
    keypad = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'J'],
        ['K', 'L', 'M', 'N', 'O'],
        [None, '1', '2', '3', None]
    ]

    # Create mapping of key -> (row, col)
    key_positions = {}
    for row in range(len(keypad)):
        for col in range(len(keypad[row])):
            if keypad[row][col] is not None:
                key_positions[keypad[row][col]] = (row, col)

    return keypad, key_positions


def get_knight_moves(row, col, keypad):
    """Get all valid knight moves from a given position."""
    # Knight move offsets: 2 vertical + 1 horizontal, or 2 horizontal + 1 vertical
    knight_offsets = [
        (-2, -1), (-2, 1),  # 2 up, 1 left/right
        (2, -1), (2, 1),  # 2 down, 1 left/right
        (-1, -2), (-1, 2),  # 1 up, 2 left/right
        (1, -2), (1, 2)  # 1 down, 2 left/right
    ]

    valid_moves = []
    for dr, dc in knight_offsets:
        new_row, new_col = row + dr, col + dc
        # Check if the new position is within bounds and not None
        if (0 <= new_row < len(keypad) and
                0 <= new_col < len(keypad[new_row]) and
                keypad[new_row][new_col] is not None):
            valid_moves.append(keypad[new_row][new_col])

    return valid_moves


def build_adjacency_graph(keypad, key_positions):
    """Build a graph of valid knight moves from each key."""
    graph = {}
    for key, (row, col) in key_positions.items():
        graph[key] = get_knight_moves(row, col, keypad)
    return graph


def is_vowel(key):
    """Check if a key is a vowel."""
    return key in ['A', 'E', 'I', 'O']


def count_sequences(graph, sequence_length=10, max_vowels=2):
    """
    Count valid sequences using dynamic programming.

    State: (current_key, length, vowel_count)
    dp[key][length][vowels] = number of valid sequences ending at 'key'
                               with 'length' keys pressed and 'vowels' vowels used
    """
    # Initialize DP table
    dp = {}

    # Base case: sequences of length 1
    for key in graph.keys():
        vowel_count = 1 if is_vowel(key) else 0
        if vowel_count <= max_vowels:
            dp[(key, 1, vowel_count)] = 1

    # Build up sequences of increasing length
    for length in range(2, sequence_length + 1):
        for key in graph.keys():
            for vowel_count in range(max_vowels + 1):
                count = 0

                # Look at all keys that can reach this key via knight move
                for prev_key in graph.keys():
                    if key in graph[prev_key]:
                        # Calculate previous vowel count
                        prev_vowel_count = vowel_count - (1 if is_vowel(key) else 0)

                        # Check if this transition is valid
                        if prev_vowel_count >= 0:
                            prev_state = (prev_key, length - 1, prev_vowel_count)
                            if prev_state in dp:
                                count += dp[prev_state]

                if count > 0:
                    dp[(key, length, vowel_count)] = count

    # Sum all valid sequences of the target length
    total = 0
    for key in graph.keys():
        for vowel_count in range(max_vowels + 1):
            state = (key, sequence_length, vowel_count)
            if state in dp:
                total += dp[state]

    return total


def main():
    """Main function to solve the problem."""
    keypad, key_positions = build_keypad()
    graph = build_adjacency_graph(keypad, key_positions)

    # Find all valid 10-key sequences with at most 2 vowels
    result = count_sequences(graph, sequence_length=10, max_vowels=2)

    print(result)


if __name__ == "__main__":
    main()