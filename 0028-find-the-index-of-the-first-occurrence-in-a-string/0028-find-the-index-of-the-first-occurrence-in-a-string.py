class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #first we neeed to construct the LPS (longest proper prefix that is also a suffix) array for the pattern (same length as pattern). 

#initialize lps[0] = 0 = previousLPS since a 0 length string doesn't have any valid LPS. 
        
        #we will have two pointers, one tracking the previousLPS, one the current index in the pattern
        #there are 3 cases:
        #1. if the pattern[previousLPS] == pattern[current_index] (here previousLPS actually points to next element we are checking for LPS)
        #just increament previousLPS store it lps[current_index] and increment current_index
        #2. if the pattern[previousLPS] != pattern[current_index] if previousLPS was 0 just set lps[current_index] = 0 
        #3. Otherwise if they were not equal and previousLPS was not 0, set previousLPS = lps[previousLPS-1]
        
        
        def find_lps(needle):
            n = len(needle)
            lps = [0 for i in range(n)]
            prev_lps = lps[0] = 0
            i=1
            while i<n:
                if needle[prev_lps] == needle[i]:
                    lps[i] = prev_lps+1
                    prev_lps+=1
                    i+=1
                elif prev_lps == 0:
                    lps[i] = 0
                    i+=1
                else:
                    prev_lps = lps[prev_lps-1] #here prev_lps was pointing to next elem to be compared from the beginning of the string and also the total number of elements that got matched so far
                    #we are actually matching here as well using the previous lps
            return lps
        
        lps = find_lps(needle)
        i, j = 0, 0
        n = len(needle)
        while i<len(haystack):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
                if j == n:
                    return i-j
            elif j!=0:
                j = lps[j-1]
            else:
                i+=1
        return -1
            
        
        
        
        
        