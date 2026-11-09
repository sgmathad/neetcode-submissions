class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = dict()
        self.first = None
        self.last = None

    def remove_front(self):
        self.first = self.first.next
        self.first.prev = None
    
    def add_last(self, node: Node):
        if not self.first:
            self.last = self.first = node
            return

        self.last.next = node
        node.prev = self.last
        self.last = node

    def update(self, node: Node, val: None | int = None):
        if val:
            node.val = val
        
        if node == self.last:
            return
        
        if node == self.first:
            self.remove_front()
        
        else:
            prev = node.prev
            _next = node.next
            prev.next = _next
            _next.prev = prev
        
        node.next = None
        self.add_last(node)

        
    def get(self, key: int) -> int:
        if key in self.store:
            node = self.store[key]
            self.update(node)
            return node.val
        
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.update(self.store[key], value)
            return
        
        node = Node(key, value)
        self.store[key] = node
        self.add_last(node)

        if len(self.store) > self.capacity:
            node = self.first
            self.remove_front()
            del self.store[node.key]
        
        

        
