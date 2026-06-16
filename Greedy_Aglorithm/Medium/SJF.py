# Shortest Job first
"""
The shortest job first (SJF) or shortest job next, is a 
scheduling policy that selects the waiting process with the 
smallest execution time to execute next. Given an array of 
integers bt[] of size n. Array bt[] denotes the burst time of 
each process. Calculate the average waiting time of all the 
processes and return the nearest integer which is smaller or 
equal to the output.

Note: Consider all process are available at time 0.

Examples:

Input: bt[] = [4,3,7,1,2]
Output: 4
Explanation: After sorting burst times by shortest job 
policy, calculated average waiting time is 4.
"""

# Optimal solution using greedy approach and traversin array
# TC = O(N) traversing array + O(NlogN) sorting = O(NlogN) and SC = O(1) 
def sjf(burstTime:list[int]) -> int:
    burstTime.sort()
    waitTime = 0
    time = 0
    for i in range(len(burstTime)):
        waitTime += time
        time += burstTime[i]
    return waitTime//len(burstTime)
