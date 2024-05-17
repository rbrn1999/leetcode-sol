# link: https://leetcode.com/problems/accounts-merge/

# DFS
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        adj = defaultdict(list)
        # make mails in the same account connected
        for account in accounts:
            root_mail = account[1]
            for mail in account[2:]:
                adj[mail].append(root_mail)
                adj[root_mail].append(mail)

        def dfs(mail: str, visited: set):
            if mail in visited:
                return

            visited.add(mail)
            for other_mail in adj[mail]:
                dfs(other_mail, visited)

        result = []
        visited = set()
        for account in accounts:
            if account[1] not in visited:
                new_mails = set()
                dfs(account[1], new_mails)
                result.append([account[0]] + sorted(new_mails))
                visited.update(new_mails)

        return result


# Union Find
from collections import defaultdict
class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, node: int) -> int:
        p = self.par[node]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]

        return p

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1

        return True

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        result = []
        name_accounts = defaultdict(list)
        for account in accounts:
            name_accounts[account[0]].append(account)

        for name in name_accounts:
            n = len(name_accounts[name])
            unionFind = UnionFind(n)
            email_owner = {}
            for i in range(n):
                for email in name_accounts[name][i][1:]:
                    if email not in email_owner:
                        email_owner[email] = i
                    else:
                        unionFind.union(i, email_owner[email])

            merged_accounts = defaultdict(list)
            for email in email_owner:
                i = unionFind.find(email_owner[email])
                merged_accounts[i].append(email)

            for emails in merged_accounts.values():
                result.append([name] + sorted(emails))

        return result
