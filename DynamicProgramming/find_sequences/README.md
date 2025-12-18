## Find Sequences - Dynamic Programming Approach

The key observation is that to count sequences of length `k` ending at position `(i, j)` with `v` vowels, we only need to know:
- How many sequences of length `k-1` end at positions that can reach `(i, j)` via a knight move
- The vowel count of those previous sequences

### State Definition

We define our DP state as:
```
states[(i, j)][seq_len % 2][vowel_count] = number of sequences
```

Where:
- `(i, j)` = ending position on the keypad
- `seq_len % 2` = sequence length modulo 2 (we only need 2 states due to space optimization)
- `vowel_count` = number of vowels in the sequence (0, 1, or 2)

### Space Optimization

Since we only need the previous sequence length to compute the current one, we use a **rolling array** technique:
- Instead of storing states for all sequence lengths (1 to 10), we only store 2 states
- We alternate between `states[pos][0]` and `states[pos][1]` using modulo 2
- This reduces space from `O(positions × 10 × 3)` to `O(positions × 2 × 3)`

### Algorithm Steps

#### 1. State Initialization and Graph Building

**Note**: Since knight moves are symmetric (if A can reach B via a knight move, then B can reach A via the reverse knight move), when we iterate through `graph[(i, j)]`, we're effectively getting the positions that can reach `(i, j)` due to this symmetry.

#### 2. DP Transitions
To form a sequence of length `k` ending at `(i, j)` with `v` vowels:
  - We need sequences of length `k-1` ending at positions that can reach `(i, j)`
  - If `(i, j)` is a vowel, the previous sequences must have `v-1` vowels
  - If `(i, j)` is not a vowel, the previous sequences must have `v` vowels

#### 3. Final Answer
Sum all states for sequences of length 10.


### Complexity Analysis

- **Time Complexity**: O(positions × sequence_length × vowel_counts × avg_knight_moves)

- **Space Complexity**: O(positions × 2 × 3) = **O(108)** states

