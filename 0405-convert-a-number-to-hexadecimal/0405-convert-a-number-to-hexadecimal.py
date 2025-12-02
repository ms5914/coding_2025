class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return "0"

        bin_to_hex = ["0", "1", "2", "3", "4", "5" , "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        result = []

        #anding with 32 1s integers in python can be infinite something like that to fix that (this is not requried in java)
        num = num & 0xffffffff
        while num:
            last_four = num & 15
            result.append(bin_to_hex[last_four])
            num = num >> 4
        return "".join(result[::-1])


        
# class Solution:
#     def toHex(self, num: int) -> str:
#         if num == 0:
#             return "0"
        
#         # '0123456789abcdef' acts as our map
#         hex_map = "0123456789abcdef"
#         result = ""
        
#         # Standardize to 32-bit integer to handle negative numbers like Java's >>>
#         # This converts -1 to 4294967295 (0xFFFFFFFF)
#         num &= 0xFFFFFFFF
        
#         while num != 0:
#             # num & 15 is equivalent to num % 16
#             result = hex_map[num & 15] + result
            
#             # Right shift by 4 bits (divide by 16)
#             num >>= 4
            
#         return result