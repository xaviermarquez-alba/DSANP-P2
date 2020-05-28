from copy import deepcopy


class Node(object):
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


class DLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.elem_count = 0

    def add(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail    # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next   # shift the tail (i.e., the back of the queue)

        self.elem_count += 1
    
    def remove_head(self):
        if self.head:
            head_key = self.head.key
            self.head = self.head.next
            self.elem_count -= 1

            return head_key

        return None

    def delete_node(self, Node):
        if Node is self.head:
            self.head = Node.next
            Node.next.prev = None
        elif Node is self.tail:
            self.tail = Node.prev
            Node.prev.next = None
        else:
            Node.next.prev = Node.prev
            Node.prev.next = Node.next
        self.elem_count -= 1

    def show_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, current_node.prev, current_node.next)
            current_node = current_node.next
        print('---------------------------------------')
        print('cantidad',self.elem_count)


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict()
        self.list_cache = DLinkedList()
        self.max_size = capacity - 1

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            value = self.cache[key].value
            self.list_cache.delete_node(self.cache[key])
            self.list_cache.add(self.cache[key])

            return value

        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.cache:
            self.cache[key].value = value
            self.list_cache.delete_node(self.cache[key])
            self.list_cache.add(self.cache[key])

        else:
            if self.list_cache.elem_count > self.max_size:
                remove_key = self.list_cache.remove_head()
                del self.cache[remove_key]
            
            self.cache[key] = Node(value, key)
            self.list_cache.add(self.cache[key])
            

    def show_cache(self):
        ls = [self.list_cache, self.cache]
        return ls
        

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

t1 = our_cache.get(1)       # returns 1
t2 = our_cache.get(2)       # returns 2
t3 = our_cache.get(9)      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5) 
our_cache.set(6, 6)

t4 = our_cache.get(3)    
t5 = our_cache.get(4)
our_cache.set(7, 7) 
our_cache.set(8, 8)
t6 = our_cache.get(5)
our_cache.set(7, "siete")

t7 = our_cache.get(7)

our_cache.set(1, "uno")
our_cache.set(2, "dos")

t8 = our_cache.get(2)

print(t8)
