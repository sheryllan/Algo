"""
Implement a prototype of a resource allocation system in a distributed parallel computing infrastructure.

There are n resources and m tasks to schedule on them where the i-th task has a processing time of burstTime[i].
The total load time or a resource is the sum or the total burst times of the jobs assigned to the resources.
However, a particular resource can be allocated jobs in a contiguous segment only, i.e. from some index x to some index y or [x,x+1,x+2,...,y].

Find the minimum possible value of the maximum total load time of the server if resources are allocated optimally.

Example:
    Consider n = 3, m = 6, burstTime = [4, 3, 2, 2, 2, 6],
    servers are consume time as [[4, 3], [2, 2, 2], [6]]
    Hence, the maximum load on any machine is 4+3=7
"""


def min_max_total_load_time(n, burstTime):
    """
    Find the minimum possible value of the maximum total load time of the server.

    Parameters:
    - n (int): Number of resources.
    - burstTime (list): List of processing times for each task.

    Returns:
    - int: Minimum possible value of the maximum total load time.
    """
    def is_valid_load(limit):
        """
        Check if it is possible to allocate jobs with the given limit.
        """
        current_load = 0
        resources_count = 0

        for time in burstTime:
            current_load += time

            if current_load > limit:
                resources_count += 1
                current_load = time

        return resources_count < n

    left, right = max(burstTime), sum(burstTime)
    # binary search in the range of [max, sum]
    while left < right:
        mid = (left + right) // 2

        if is_valid_load(mid):
            right = mid
        else:
            left = mid + 1

    return left


"""
min_max_total_load_time uses binary search to efficiently find the minimum of the maximum sum of n contiguous sublists 
from the given list of burst times. 
It defines a helper function, is_valid_load, to check if it's possible to divide the burst times into n sublists such 
that the maximum sum of any sublist is less than or equal to a given threshold. 
The binary search narrows down the range of possible thresholds until the minimum is found.
The runtime complexity is o(nlog(n))
"""


burst_times = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resources = 3
result = min_max_total_load_time(resources, burst_times)
assert result == 17
print(f"The minimum of the maximum sum of {resources} sublists is: {result}")


resources = 4
burst_times = [4, 3, 2, 2, 2, 6]
result = min_max_total_load_time(resources, burst_times)
assert result == 6