"""
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n.
Each CPU interval can be idle or allow the completion of one task.
Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.



Constraints:

1 <= tasks.length <= 10e4
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""


from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        remaining_cycles = {x: 0 for x in tasks}
        cycles = 0
        last_task = None

        while counter:
            tasks_ready = []

            for task in remaining_cycles:
                if task != last_task and remaining_cycles[task] > 0:
                    remaining_cycles[task] -= 1

                if remaining_cycles[task] == 0:
                    tasks_ready.append(task)
            print(f'before cycle {cycles + 1}: {remaining_cycles}')

            tasks_sorted = sorted(tasks_ready, key=lambda x: (remaining_cycles[x], -counter[x]))

            last_task = None
            if tasks_sorted:
                curr_task = tasks_sorted[0]
                print(f'picked task {curr_task}')
                counter[curr_task] -= 1
                remaining_cycles[curr_task] += n
                if counter[curr_task] == 0:
                    counter.pop(curr_task)
                    remaining_cycles.pop(curr_task)

                last_task = curr_task
            print(f'counter {counter}')
            print(f'after cycle {cycles + 1}: {remaining_cycles}')
            cycles += 1

        return cycles



    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        remaining_cycles = {x: 0 for x in tasks}
        cycles = 0
        last_task = None

        while counter:
            max_count = 0
            selected_task = None

            for task in counter:
                if task != last_task and remaining_cycles[task] > 0:
                    remaining_cycles[task] -= 1

                if remaining_cycles[task] == 0 and counter[task] > max_count:
                    selected_task = task
                    max_count = counter[task]

            last_task = None
            if selected_task:
                counter[selected_task] -= 1
                remaining_cycles[selected_task] += n
                if counter[selected_task] == 0:
                    counter.pop(selected_task)
                    remaining_cycles.pop(selected_task)

                last_task = selected_task

            cycles += 1

        return cycles



"""
Intuition:
To solve this problem, we need to find the minimum number of intervals required to complete all tasks 
while following the cooling time constraint. 
One way to approach this is to first count the frequency of each task. 
Then, we can sort the frequencies in descending order to prioritize tasks with higher frequency. 
After sorting, we can calculate the number of intervals needed by considering the task with the maximum frequency.

Approach:

Count the frequency of each task using an array freq.
Sort the freq array in descending order.
Calculate the number of intervals needed based on the task with the maximum frequency.
Return the total number of intervals required.
Complexity:

Time complexity: Sorting the freq array takes O(26 log 26), which simplifies to O(1) as it's a constant time operation. 
The loop to calculate intervals takes O(26), which is again a constant. So overall, the time complexity is O(1).
Space complexity: We use an array of size 26 for frequency, so the space complexity is O(1).

"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort()
        chunk = freq[25] - 1
        idle = chunk * n

        for i in range(24, -1, -1):
            idle -= min(chunk, freq[i])

        return len(tasks) + idle if idle >= 0 else len(tasks)