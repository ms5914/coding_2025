class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for word in strings:
            key = ["1"]
            for ch1, ch2 in zip(word, word[1:]):
                key.append(str((ord(ch2)-ord(ch1))%26))
            mp[tuple(key)].append(word)
        return list(mp.values())
                

        