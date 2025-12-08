class Solution:
    def killProcess(self, pid, ppid, kill):
        tree = defaultdict(list)
        for i in range(len(pid)):
            parent = ppid[i]
            child = pid[i]
            tree[parent].append(child)

        killed = []
        stack = [kill]

        while stack:
            process = stack.pop()
            killed.append(process)
            children = tree[process]
            for child in children:
                stack.append(child)
        return killed