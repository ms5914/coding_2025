class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        characters = 0
        result = []

        for word in words:
            if len(res)+len(word)+characters>maxWidth:
                for i in range(maxWidth-characters):
                    res[i%((len(res)-1) or 1)]+=" "
                characters = 0
                result.append("".join(res))
                res = []
            characters+=len(word)
            res.append(word)
        
        return result + [" ".join(res) + " "*(maxWidth-len(" ".join(res)))]

            

        