## Optimize n*m states into O(m) 1d array

Assume we need to reduce the n*m 2d array "f" into a 1d array:

1. If you encountered a state function like:

    f[i][c] = f[i-1][c-w] + f[i-1][c]

    Note: f[i-1] means the last state of f before entering into the i-th outer loop.

    it means that in the inner loop, the state of c will depend on previous state of c-w in the (i-1)th the outer iteration -
    looping forward with c will have previous results override the original f[i-1] state before value c.

    Therefore, looping backward is required.

2. If you encountered a state function like:
   
    f[i][c] = min(f[i][c-w] + 1, f[i-1][c])
    
    it means that the state of c is dependent on the cascading results of c-w in this i-th outer iteration.
    
    Therefore, looping forward is necessary.

3. If you encountered a state function like:

    f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
    
    Due to f[i][j-1] cascading result bit, it must loop forward. 

    However, as j goes forward, it would override f[i-1][j-1].
    
    Therefore, before assigning f[j], we need to record the value before change, save it for use in the calculation of f[j+1]

    

