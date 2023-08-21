# link: https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

from collections import defaultdict

class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        group_items = defaultdict(list)
        for i in range(n):
            if group[i] >= 0:
                group_items[group[i]].append(i)
            else:
                group_items[-i-1].append(i)
                group[i] = -i-1

        beforeGroups = defaultdict(set)
        group_order = []
        for i in range(n):
            for prev in beforeItems[i]:
                if group[prev] == group[i]:
                    continue
                else:
                    beforeGroups[group[i]].add(group[prev])
            
        visited = set()
        processing = set()
        def dfs(i: int, arr: [int]):
            if i in visited:
                return True
            if i in processing:
                return False
            processing.add(i)
            for j in beforeGroups[i]:
                if not dfs(j, arr):
                    return False
            arr.append(i)
            processing.remove(i)
            visited.add(i)
            return True
        

        def dfs_items(i: int, group_num: int, before_group: [int], in_group: [int]):
            if i in visited:
                return True
            if i in processing:
                return False
            processing.add(i)
            for j in beforeItems[i]:
                if group[i] == -1 and group[j] == group_num \
                or not dfs_items(j, group_num, before_group, in_group):
                    return False
            if group[i] == group_num:
                in_group.append(i)
            else:
                before_group.append(i)
            processing.remove(i)
            visited.add(i)
            return True

        group_order = []
        for g in group_items:
            if not dfs(g, group_order):
                return []

        items = []
        visited.clear()
        processing.clear()
        
        for g in group_order:
            for i in group_items[g]:
                before, in_group = [], []
                if dfs_items(i, g, before, in_group):
                    items += before + in_group
                else:
                    return []
        return items