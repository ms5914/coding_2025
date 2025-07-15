class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = defaultdict(int)
        min_window = float("inf")
        start = end = -1
        matched_chars=0
        total_chars = len(t_count)
        i = 0
        for j, ch in enumerate(s):
            if ch in t_count:
                s_count[ch]+=1
                if s_count[ch] == t_count[ch]:
                    matched_chars+=1
                while matched_chars == total_chars:
                    if j-i+1 < min_window:
                        min_window = j-i+1
                        start = i
                        end = j  
                    if s[i] in s_count and s[i] in t_count:
                        if s_count[s[i]] == t_count[s[i]]:
                            matched_chars-=1
                        s_count[s[i]]-=1
                        if s_count[s[i]] == 0:
                            del s_count[s[i]]
                    i+=1
        return s[start:end+1] if min_window != float("inf") else ""


                        