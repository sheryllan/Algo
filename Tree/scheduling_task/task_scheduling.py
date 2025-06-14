"""
The key insight is that the task with a later deadline MUST be completed later than a task with an earlier deadline -
regardless how you break up the tasks.
Otherwise, the first task (the one with an earlier deadline) will overshoot its own deadline by more than the second task overshoots its deadline.
So we can essentially just sort the tasks by their deadline and complete them in that order.
The problem description about breaking up tasks are just there to confuse you. (why?)

However, since the problem requires you to do this incrementally, i.e., solve the scheduling for tasks from 1 to n.
The naive method above takes O(nlog(n)) for each iteration, so it will take O((n^2)log(n)) in total, which is unacceptable:
a solution in Python only has 16 seconds to solve the problem.
So a more efficient solution is needed. This is turns out to be quite hard.

The key difficulty is that when inserting a new task, all tasks that follows the newly inserted task must have their
completion time (and overtime) updated. That is the part that causes the O(n^2) behavior.
It turns out that there is a data structure to do this efficiently, it is called a Binary Indexed Tree.
Secondly, we also need to keep track of the max overtime for three ranges, the tasks before the new tasks,
the new task itself, and tasks after the new task.
This problem is known as the "range-minimum-query" and a data structure called Segment Tree.
"""


import os


#
# Complete the 'taskScheduling' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER m
#

def taskScheduling(d, m):
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = taskScheduling(d, m)

        fptr.write(str(result) + '\n')

    fptr.close()
