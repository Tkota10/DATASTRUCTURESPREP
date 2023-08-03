class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.cache = {} # Important to Map key to Node
        self.cap = capacity

        self.left = Node(0, 0) # Left is least recent
        self.right = Node(0, 0) # Right is most recent
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        if key in self.cache: # A node already exists with this same key value
            self.remove(self.cache[key]) # Remove the node that already exists
        self.cache[key] = Node(key, value) # Create a new Node in the cache
        self.insert(self.cache[key]) # Then Inserting it into the doubly linked list
        if len(self.cache) > self.cap:
            lru = self.left.next #Accesing the old Left elemeent
            self.remove(lru)
            del self.cache[lru.key] 