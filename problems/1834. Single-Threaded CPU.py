# link: https://leetcode.com/problems/single-threaded-cpu/

'''
Sorting + Min-Heap
Time Complexity: O(nlog(n))
Space Complexity: O(n)
'''
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = [] #(processTime, id)
        time = 0
        n = len(tasks)
        sorted_tasks = sorted([(tasks[i][0], tasks[i][1], i) for i in range(n)], reverse=True)
        def pushTasks(time):
            while sorted_tasks and time >= sorted_tasks[-1][0]:
                task_enqueueTime, task_processTime, task_id = sorted_tasks.pop()
                heapq.heappush(heap, (task_processTime, task_id))

        result = []
        while heap or sorted_tasks:
            if not heap:
                time = max(time, sorted_tasks[-1][0])
            pushTasks(time)
            processTime, task_id = heapq.heappop(heap)
            time += processTime
            result.append(task_id)

        return result


