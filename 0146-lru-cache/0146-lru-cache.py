class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not key in self.hm:
            return -1
        node = self.hm[key]
        val = node.val

        #removing node
        prev_node = node.prev
        next_node = node.next
        prev_node.next= next_node
        next_node.prev = prev_node

        #adding node
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node

        return val

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.hm:
            node = self.hm[key]
            node.val = value
            
            #removing node
            prev_node = node.prev
            next_node = node.next
            prev_node.next= next_node
            next_node.prev = prev_node

        else:
            node = Node(key, value)
            self.hm[key] = node
        
        #adding node
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node

        if len(self.hm) > self.capacity:
            head_next = self.head.next
            head_next.prev.next = head_next.next
            head_next.next.prev = self.head
            del self.hm[head_next.key]
        






            



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)