class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        
        def iptobin(ip):
            return "".join(["{:08b}".format(int(number)) for number in ip.split(".")])

        def bintoip(bin):
            return ".".join([str(int(bin[i:i+8],2)) for i in range(0, 32, 8)])
        
        curr_ip = iptobin(ip)
        ans = []

        while n:
            i = len(curr_ip)-1
            num_zeros = 0
            
            while i>=0 and curr_ip[i] == "0":
                num_zeros+=1
                i-=1
            while pow(2, num_zeros) > n:
                num_zeros-=1
            
            ans.append(bintoip(curr_ip)+"/"+str(32-num_zeros))
            n-=pow(2, num_zeros)
            curr_ip = "{:032b}".format(int(curr_ip, 2)+pow(2, num_zeros))
        return ans
            
            
            
            



        


        