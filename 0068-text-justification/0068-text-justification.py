class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        results=[]
        res=[]
        starting=0
        characters=0
        for word in words:
            if len(word)+len(res)+characters>maxWidth:
                for i in range(maxWidth-(characters)):
                    res[i%(len(res)-1 or 1)]+=' '
                results.append(''.join(res))
                characters=0
                res=[]
            characters+=len(word)
            res.append(word)
        return results+[' '.join(res).ljust(maxWidth)]
        