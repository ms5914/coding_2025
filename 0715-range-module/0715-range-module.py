import bisect
class RangeModule:

    def __init__(self):
        self.arr = []
        

    def addRange(self, left: int, right: int) -> None:
        l,r = bisect.bisect_left(self.arr, left), bisect.bisect_right(self.arr, right)
        temp =[]
        if l%2==0:
            temp.append(left)
        if r%2==0:
            temp.append(right)
        self.arr[l:r] = temp
        

    def queryRange(self, left: int, right: int) -> bool:
        l,r =  bisect.bisect_right(self.arr, left), bisect.bisect_left(self.arr, right)
        return l==r and l%2==1


    def removeRange(self, left: int, right: int) -> None:
        l,r = bisect.bisect_left(self.arr, left), bisect.bisect_right(self.arr, right)
        temp =[]
        if l%2==1:
            temp.append(left)
        if r%2==1:
            temp.append(right)
        self.arr[l:r] = temp


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)