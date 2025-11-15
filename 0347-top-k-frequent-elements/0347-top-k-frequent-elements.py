class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums)
        unique = list(count_map.keys())
        n = len(nums)
        unique_n = len(unique)

        def partition(left, right):
            if left>right:
                return
            index = random.randint(left, right)
            index_freq = count_map[unique[index]]
            unique[index], unique[right] = unique[right], unique[index]

            left_index = left
            for i in range(left, right):
                if count_map[unique[i]]< index_freq:
                    unique[left_index], unique[i] = unique[i], unique[left_index]
                    left_index+=1
            unique[left_index], unique[right] = unique[right], unique[left_index]
            return left_index
        
        def find_k_frequent(left, right):
            if left > right:
                return
            piv_index = partition(left, right)
            if index == unique_n-k:
                return
            elif piv_index<unique_n-k:
                find_k_frequent(piv_index+1, right)
            else:
                find_k_frequent(left, piv_index-1)
        
        find_k_frequent(0, unique_n-1)
        return unique[unique_n-k:]
        
        







