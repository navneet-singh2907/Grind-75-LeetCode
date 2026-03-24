class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution:
    def accountsMerge(self, accounts):
        uf = UnionFind(len(accounts))
        email_to_acc = {} # email -> index of account

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email_to_acc:
                    uf.union(i, email_to_acc[email])
                else:
                    email_to_acc[email] = i
        
        # Group emails by their root account index
        from collections import defaultdict
        merged = defaultdict(list)
        for email, acc_idx in email_to_acc.items():
            root = uf.find(acc_idx)
            merged[root].append(email)
            
        # Format the final result
        res = []
        for root, emails in merged.items():
            name = accounts[root][0]
            res.append([name] + sorted(emails))
        return res
