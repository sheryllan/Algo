"""
I have a list of costs and time required for each task.
I have two servers to run those jobs, where one is paid and the other one is free.
To use the free server you have to run a task on the paid one.
The paid server takes as much time mentioned in the time array, while the free server can run any task in 1 unit of time.
I have to find the minimum cost to run all the jobs with the given constraints.
"""

"""the crux here is to identify for the ith task, the time and cost taking the task into consideration is"
if running on paid server:
remaining_free_time += time[i]
cost += cost[i]

if running on free server:
remaining_free_time -=1
cost = cost

and we nee to take a min these two.



Top down is usually easiest. "Write a recursive function, memoize." Here is an untested recursive function.

def cost_at (idx, free_time_left):
    if idx == len(cost):
        if 0 <= free_time_left:
            return 0
        else:
            return float('inf')
    else:
        cost_paid = cost_at(idx+1, free_time_left + time[idx]) + cost[idx]
        cost_unpaid = cost_at(idx+1, free_time_left - 1)
        return min(cost_paid, cost_unpaid)
And now memoize.

def cost_at (idx, free_time_left):
    if idx == len(cost):
        if 0 <= free_time_left:
            return 0
        else:
            return float('inf')
    else:
        if (idx, free_time_left) not in cache:
            cost_paid = cost_at(idx+1, free_time_left + time[idx]) + cost[idx]
            cost_unpaid = cost_at(idx+1, free_time_left - 1)
            cache[(idx, free_time_left)] = min(cost_paid, cost_unpaid)
        return cache[(idx, free_time_left)]
There are lots of libraries that let you simply cache things and not worry too much about the structure of the cache. But the structure matters. This cache can be written in various ways but all boil down to:

by idx
    by free time left
        cost
This is a depth first search with caching. To mechanically turn this into a bottom up solution we need to switch to a breadth first search.

That is we need to switch to finding what all of the possibilities are for idx = 0, then idx = 1, and so on. 
But with a twist. The top down solution stores the best cost FROM this point on. 
The bottom up solution stores the best cost TO this point. So something like this (untested)
"""


def get_min_cost(costs, times):
    N = len(times)
    current_state = {N: None}  # assuming all tasks running on free server
    for i in range(N):
        prev_state = current_state.copy()
        for total_free_time, cost in prev_state.items():
            if total_free_time <= 0:  # no need to add more paid server as all the free server time is covered
                continue
            # using paid server
            free_time_paid = total_free_time - times[i] - 1
            cost_paid = (cost + costs[i]) if cost is not None else costs[i]

            if free_time_paid not in prev_state or prev_state[free_time_paid] is None or cost_paid < prev_state[free_time_paid]:
                current_state[free_time_paid] = cost_paid
            # the objective is to reduce total_free_time <= 0

    return min(c for t, c in current_state.items() if t <= 0)


print(get_min_cost([1, 2, 3, 2], [1, 2, 3, 2]))
print(get_min_cost([1, 5, 2, 2, 3], [2, 4, 2, 1, 3]))
print(get_min_cost([1, 5, 4, 2, 3], [2, 4, 2, 1, 3]))
print(get_min_cost([1, 5, 4, 2, 2, 1, 2], [2, 4, 2, 1, 4, 1, 1]))


"""
Bottom up is its own skill. We are currently storing every relationship prev_state[free_time_left] = prev_cost which is the same as storing a bunch of pairs (free_time_left, prev_cost). 
But we don't actually need to store EVERY one of these pairs. 
We can get rid of any pair where there is another pair with the same or more free_time_left, and the same or less prev_cost. 
Because that other solution will lead to an best answer that cannot be worse than this one, so this one can be dropped immediately.

This leads to the idea of an optimal fringe, where we have an array of [(time1, cost1), (time2, cost2), ...] stored by increasing time and decreasing cost. 
That lets us do the following (again untested).

def min_cost():
    fringe = [(0, 0)]
    for idx in range(len(cost)):
        fringe_unused = [(x[0]-1, x[1]) for x in fringe]
        fringe_used = [(x[0]+time[idx], x[1]+cost[idx]) for x in fringe]
        fringe = []
        i = 0
        j = 0
        while i < len(fringe_unused) and j < len(fringe_used):
            # Find which pair to add to the fringe next.
            if i < len(fringe_unused):
                if len(fringe_used) <= j or fringe_unused[i][0] < fringe_used[j][0]:
                    pair = fringe_unused[i]
                    i += 1
                else:
                    pair = fringe_used[j]
                    j += 1
            else:
                pair = fringe_used[j]
                j += 1
            
            # Remove the pairs in the fringe that are worse than this.
            while 0 < len(fringe) and pair[1] <= fringe[-1][1]:
                fringe.pop()
            # And add it.
            fringe.append(pair)
    i = 0
    while fringe[i][0] < 0:
        i += 1
    return fringe[i][1]
While the previous bottom up solution saved memory but not time, THIS one saves BOTH memory AND time. 
Because it avoids looking at possibilities that can't lead to an optimal solution.
"""