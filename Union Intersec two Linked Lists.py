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

def union(llist_1, llist_2):
    # Your Solution Here
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
    # Your Solution Here
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


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

