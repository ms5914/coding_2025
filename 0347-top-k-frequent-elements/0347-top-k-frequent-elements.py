class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums)
        unique_elements = list(count_map.keys())
        n = len(unique_elements)
        print(count_map)
        print(unique_elements)

        def partition(A, p, r):
            if p>r:
                return
            
            ind = random.randint(p,r)
            print(ind)
            freq = count_map[A[ind]]
            A[ind], A[r] = A[r], A[ind]

            k = p
            for i in range(p, r):
                if count_map[A[i]] < freq:
                    A[k], A[i] = A[i], A[k]
                    k+=1
            A[k], A[r] = A[r], A[k]
            
            return k
        

        def find_top_k(A, p, r):
            if p>=r:
                return
            ind = partition(A, p, r)

            if ind == n-k:
                return
            elif ind < n-k:
                find_top_k(A, ind+1, r)
            else:
                find_top_k(A, p, ind-1)
        
        find_top_k(unique_elements, 0, n-1)
        return unique_elements[n-k:]
                




