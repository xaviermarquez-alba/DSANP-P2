class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def get_list(self):
        cur_head = self.head
        out_list = []
        while cur_head:
            out_list.append(cur_head.value) 
            cur_head = cur_head.next
        return out_list


def union(llist_1, llist_2):
    union_set = set()
    current_node_l1 = llist_1.head

    while current_node_l1:
        union_set.add(current_node_l1.value)
        current_node_l1 = current_node_l1.next

    current_node_l2 = llist_2.head
    
    while current_node_l2:
        union_set.add(current_node_l2.value)
        current_node_l2 = current_node_l2.next
    
    union_link_list = LinkedList()
    for item in union_set:
        union_link_list.append(item)

    return union_link_list

def intersection(llist_1, llist_2):
    intersection_set = set()

    current_node_l1 = llist_1.head
    list1_set = set()
    while current_node_l1:
        list1_set.add(current_node_l1.value)
        current_node_l1 = current_node_l1.next

    current_node_l2 = llist_2.head
    while current_node_l2:
        if current_node_l2.value in list1_set:
            intersection_set.add(current_node_l2.value)
        current_node_l2 = current_node_l2.next
    
    intersection_link_list = LinkedList()
    for item in intersection_set:
        intersection_link_list.append(item)

    return intersection_link_list

def test_union_intersection(list1, list2):
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    
    for i in list1:
        linked_list_1.append(i)

    for i in list2:
        linked_list_2.append(i)

    # Test Union 
    union1 = union(linked_list_1,linked_list_2)
    union1_list = union1.get_list()

    # python Union function
    py_union1 = list(set(list1).union(set(list2)))

    if sorted(py_union1) == sorted(union1_list):
        print('*** Test Pass: Union List ***')
        print(union1)
    else:
        print('*** Test Fail: Union List ***')

    # Test Intersection 
    intersection1 = intersection(linked_list_1,linked_list_2)
    intersection1_list = intersection1.get_list()
    
    # python Intersect function
    py_intersection1 = list(set(list1).intersection(set(list2)))

    if sorted(py_intersection1) == sorted(intersection1_list):
        print('*** Test Pass: Intersection List ***')
        print(intersection1)
    else:
        print('*** Test Fail: Intersection List ***')

    print('\n')
# Test case 1, Normal case

l1 = [3,2,4,35,6,64,6,4,3,21,33,45,6,7,2,34,56,13,56,7,8,9,0,31,5,12,5]
l2 = [6,32,4,9,6,1,11,21,1,4,6,78,1,80,215,6,215,61,5]
print('Test 1 Normal case')
test_union_intersection(l1,l2)


# Test case 2, List 1 empty

l1 = []
l2 = [6,32,4,9,6,1,11,21,1,4,6,78,1,80,215,6,215,61,5]
print('Test 2, List 1 empty')
test_union_intersection(l1,l2)

# Test case 3, List 1,2 empty

l1 = []
l2 = []
print('Test 3 List 1,2 empty')
test_union_intersection(l1,l2)

# Test case 4, intersection null

l1 = ['A','B','C']
l2 = [1,2,3,4]
print('Test 4 intersection null')
test_union_intersection(l1,l2)

# Test case 5, None item
l1 = [None, 1]

l2 = [1,2,3,4]

print('Test 5 None item')
test_union_intersection(l1,l2)
