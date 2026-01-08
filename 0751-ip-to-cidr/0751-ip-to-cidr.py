class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        def ip_to_bin(ip):
            return "".join(["{:08b}".format(int(x)) for x in ip.split(".")])
        def bin_to_ip(bin):
            return ".".join(str(int(bin[i:i+8], 2)) for i in range(0, 32, 8))

        result = []
        ip_bin = ip_to_bin(ip)
        while n>0:
            print(n)
            i = len(ip_bin)-1
            count_zeros = 0
            
            while i>=0 and ip_bin[i] == "0":
                count_zeros+=1
                i-=1
            
            while pow(2, count_zeros) > n:
                count_zeros-=1
            
            result.append(bin_to_ip(ip_bin)+"/"+str(32-count_zeros))
            n-=pow(2, count_zeros)
            ip_bin = "{:032b}".format(int(ip_bin, 2)+pow(2, count_zeros))
        
        return result

                
                    
                    



                


                