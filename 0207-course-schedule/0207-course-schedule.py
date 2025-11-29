class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        course_pre = defaultdict(list)
        indegree = defaultdict(int)
        dq = deque()
        visited = set()

        for pre_req in prerequisites:
            course_pre[pre_req[1]].append(pre_req[0])
            indegree[pre_req[0]]+=1
        
        for key in range(numCourses):
            if indegree[key] == 0:
                dq.append(key)
                visited.add(key)
        
        while dq:
            course = dq.popleft()
            for nei in course_pre[course]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    dq.append(nei)
                    visited.add(nei)
        
        return len(visited) == numCourses

        