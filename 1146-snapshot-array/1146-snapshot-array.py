class SnapshotArray:

    def __init__(self, length: int):
        self.index_val_map = defaultdict(list)
        self.curr_snap_id = 0
        for i in range(length):
            self.index_val_map[i].append([-1, 0])
        
        

    def set(self, index: int, val: int) -> None:
        if self.index_val_map[index] and self.index_val_map[index][-1][0] == self.curr_snap_id:
            self.index_val_map[index][-1][1] = val
        else:
            self.index_val_map[index].append([self.curr_snap_id, val])
        
    def snap(self) -> int:
        self.curr_snap_id+=1
        return self.curr_snap_id-1
        
    def get(self, index: int, snap_id: int) -> int:
        ind_changes = self.index_val_map[index]
        change_index = bisect.bisect_right(ind_changes, snap_id, key = lambda x:x[0])
        return ind_changes[change_index-1][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)