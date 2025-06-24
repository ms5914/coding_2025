class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        w, a = 0, 0

        while w < len(word) and a < len(abbr):
            if word[w] == abbr[a]:
                w+=1
                a+=1
            elif abbr[a].isdigit():
                if int(abbr[a]) == 0:
                    return False
                s = 0
                while a<len(abbr) and abbr[a].isdigit():
                    s = s*10+(ord(abbr[a])-ord('0'))
                    a+=1
                w+=s

            else:
                return False
        return a == len(abbr) and w == len(word)
    
                