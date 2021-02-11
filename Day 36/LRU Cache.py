#GeeksForGeeks Code

# Class for a Doubly LinkedList Node
class DLLNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
 
# LRU cache class
class LRUCache:
 
    def __init__(self, capacity):
        # capacity:  capacity of cache
        # Intialize all variable
        self.capacity = capacity
        self.map = {}
        self.head = DLLNode(0, 0)
        self.tail = DLLNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0
 
    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
 
    def addToHead(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node
 
    # This method works in O(1)
    def get(self, key):
        if key in self.map:
            node = self.map[key]
            result = node.val
            self.deleteNode(node)
            self.addToHead(node)
            print('Got the value : {} for the key: {}'.format(result, key))
            return result
        print('Did not get any value for the key: {}'.format(key))
        return -1
 
    # This method works in O(1)
    def set(self, key, value):
        print('going to set the (key, value) : ( {}, {})'.format(key, value))
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.deleteNode(node)
            self.addToHead(node)
        else:
            node = DLLNode(key, value)
            self.map[key] = node
            if self.count < self.capacity:
                self.count += 1
                self.addToHead(node)
            else:
                del self.map[self.tail.prev.key]
                self.deleteNode(self.tail.prev)
                self.addToHead(node)
 
 
if __name__ == '__main__':
    print('Going to test the LRU Cache Implementation')
    cache = LRUCache(2)
 
    # it will store a key (1) with value
    # 10 in the cache.
    cache.set(1, 10)
 
    # it will store a key (1) with value 10 in the cache.
    cache.set(2, 20)
    print('Value for the key: 1 is {}'.format(cache.get(1)))  # returns 10
 
    # evicts key 2 and store a key (3) with
    # value 30 in the cache.
    cache.set(3, 30)
 
    print('Value for the key: 2 is {}'.format(
        cache.get(2)))  # returns -1 (not found)
 
    # evicts key 1 and store a key (4) with
    # value 40 in the cache.
    cache.set(4, 40)
    print('Value for the key: 1 is {}'.format(
        cache.get(1)))  # returns -1 (not found)
    print('Value for the key: 3 is {}'.format(cache.get(3)))  # returns 30
    print('Value for the key: 4 is {}'.format(cache.get(4)))  # returns 40
