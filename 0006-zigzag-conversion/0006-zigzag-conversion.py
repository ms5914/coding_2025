class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = []
        if numRows == 1:
            return s
        for row_num in range(numRows):
            i = row_num
            down = True
            while i<len(s):
                # print(i)
                ans.append(s[i])
                # print("row_num", row_num)
                if row_num == 0 or row_num == numRows-1:
                    i+=2*(numRows-1)
                else:
                    if down:
                        i+=2*(numRows-1-row_num)
                        down = False
                    else:
                        i+=2*(row_num)
                        down = True
        return "".join(ans)




        