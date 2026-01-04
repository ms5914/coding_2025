class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:

        def ip_to_bin(ip):
            binary_str = "".join(["{:08b}".format(int(segment)) for segment in ip.split(".")])
            return binary_str
        
        def bin_to_ip(binary):
            ip = ".".join([str(int(binary[i:i+8], 2)) for i in range(0, 32, 8)])
            return ip

        result = []
        current_ip = ip_to_bin(ip)
        while n>0:
            j = len(current_ip)-1
            count_zeros = 0
            while j>=0 and current_ip[j] == "0":
                count_zeros+=1
                j-=1
            
            while pow(2, count_zeros) > n:
                count_zeros-=1
            
            result.append(bin_to_ip(current_ip)+"/"+str(32-count_zeros))
            n-=pow(2, count_zeros)
            current_ip = "{:032b}".format((int(current_ip, 2)+pow(2, count_zeros)))
        
        return result






            
            
            



        


        