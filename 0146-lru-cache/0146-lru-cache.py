class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.nodeMap = {}
        self.cap = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def addToTail(self, node):
        target = self.tail.prev
        target.next = node
        node.prev = target
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1   
        node = self.nodeMap[key]
        self.remove(node)
        self.addToTail(node)
        return node.val
    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.remove(node)
            self.addToTail(node)
            return    
        if len(self.nodeMap) >= self.cap:
            lru_node = self.head.next
            self.remove(lru_node)
            del self.nodeMap[lru_node.key]
        newNode = Node(key, value)
        self.nodeMap[key] = newNode
        self.addToTail(newNode)