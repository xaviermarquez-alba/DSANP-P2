
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
            old_tail = self.tail
            old_tail.next = new_node
            self.tail = new_node 
            new_node.next = None
            new_node.prev = old_tail

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
        first = True
        print('---------Cache Queue-----------')
        while current_node:
            if current_node.next:
                if first:
                    print('(' + str(current_node.key) + ', ' +
                      str(current_node.value) + ') <- Oldest item')
                    first = False
                else:
                    print(current_node.key, current_node.value)
            else:
                print('(' + str(current_node.key) + ', ' +
                      str(current_node.value) + ') <- Least added item')
            current_node = current_node.next

        print('---------------------------------------')


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


# Test Case 1: Discard old values when cache is full

def test_1(cache_capacity, list_items):
    print('*** Test 1: Discard old values when cache is full ***')

    our_cache = LRU_Cache(cache_capacity)

    for key, value in list_items:
        our_cache.set(key, value)

    # trying to get the first element added
    result = our_cache.get(list_items[0][1])

    # test result must be -1 (cache miss)
    assert result == -1, 'Fail Test'

    # show cache queue
    our_cache.list_cache.show_list()
    print('cache capacity: ' + str(cache_capacity) + ', Items added: ' + str(len(list_items)) + ', Item discad: ' + str(list_items[0]))
    print('*** Pass Test 1 ***')
    print('\n')


# Test Case 2: Test value when cache hit

def test_2(cache_capacity, list_items, test_key, test_value):
    print('*** Test 2: Test value when cache hit ***')

    our_cache = LRU_Cache(cache_capacity)

    for key, value in list_items:
        our_cache.set(key, value)


    # get item
    result = our_cache.get(test_key)

    # test result
    assert result == test_value, 'Fail Test'
      # show cache queue
    print('Item test: (' + str(test_key) + ", " + test_value + "), Value return for key " + str(test_key) + ": " + result )
    print('*** Pass Test 2 ***')
    print('\n')  

# Test case 3: update all cache 
def test_3(cache_capacity, list_items, list_items_new):
    print('*** Test 3: Test update all cache values ***')

    our_cache = LRU_Cache(cache_capacity)

    for key, value in list_items:
        our_cache.set(key, value)
    
    # show cache queue
    print('---------Old cache queue---------------')
    our_cache.list_cache.show_list()

    # add new items
    for key, value in list_items_new:
        our_cache.set(key, value)

    print('\n')
    print('----------New cache queue---------------')
    # new cache queue
    our_cache.list_cache.show_list()
    # test miss cache for old list
    for key, value in list_items_new:
        result = our_cache.get(key)
        assert result == value, 'Fail Test'
    
    # show cache queue
    print('*** Pass Test 3 ***')
    print('\n')  

# Test case 4: stress test 
def test_4(cache_capacity):
    print('*** Test 4: stress test***')

    our_cache = LRU_Cache(cache_capacity)

    # add numbers to 1 - 100
    for i in range(cache_capacity):
        our_cache.set(i, i)

    # get all even numbers from cache
    for i in range(2, cache_capacity, 2):
        our_cache.get(i)


    # new cache queue
    our_cache.list_cache.show_list()
    
    # show cache queue
    print('*** Pass Test 4 ***')
    print('\n')  


# Test CASE 1: test cache miss for first element (1,1)
test_1(5, [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)])


# Test CASE 2: Test value when cache hit
test_2(5, [(1,'A'),(2,'B'),(3,'C'),(4,'D'),(5,'E')], 4, 'D')


# Test CASE 3: Test value renew cache adding a new list to full capacity
test_3(5, [(1,'Old1'),(2,'Old2'),(3,'Old3'),(4,'Old4'),(5,'Old5'),(6,'Old6'),(7,'Old7')], [(1,'New1'),(2,'New2'),(3,'New3'),(4,'New4'),(5,'New5')])


# Test CASE 4: stress test 
# 1. set cache to 100 and add 100 items 
# 2. get all even numbers 
# result cache: first 50 numbers are odd numbers, last 50 items are even numbers

test_4(100)

