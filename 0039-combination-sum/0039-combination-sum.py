class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        def find_combinations(i, combination, sum_so_far):
            if sum_so_far == target:
                result.append(list(combination))
            if i>=len(candidates) or sum_so_far >= target:
                return
            
            combination.append(candidates[i])
            find_combinations(i, combination, sum_so_far+candidates[i])
            combination.pop()
            find_combinations(i+1, combination, sum_so_far)

        find_combinations(0, [], 0)
        return result