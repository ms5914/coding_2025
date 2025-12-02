class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(list)
        in_degree = {c:0 for word in words for c in word }
        for word1, word2 in zip(words[:], words[1:]):
            m, n = len(word1), len(word2)
            i, j = 0, 0
            while i<m and j<n and word1[i] == word2[j]:
                i+=1
                j+=1
            
            if i<m and j<n:
                if not word2[j] in adj_list[word1[i]]:
                    in_degree[word2[j]]+=1
                    adj_list[word1[i]].append(word2[j])
            
            elif len(word2)<len(word1):
                return ""
            
        dq = deque()
        dq = [c for c in in_degree if in_degree[c] == 0]
        visited = list(dq)

        while dq:
            letter = dq.pop()
            for neighbor in adj_list[letter]:
                in_degree[neighbor]-=1
                if in_degree[neighbor] == 0:
                    visited.append(neighbor)
                    dq.append(neighbor)
        
        if len(visited) == len(in_degree):
            return "".join(visited)
        else:
            return ""
            


        