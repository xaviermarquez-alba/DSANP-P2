import sys

def calc_string_freq(string):
    frequency_dict = dict()
    for char in string:
        char_ascii_code = ord(char)
        if char_ascii_code in frequency_dict:
            frequency_dict[char_ascii_code] += 1
        else:
            frequency_dict[char_ascii_code] = 1

    return frequency_dict

# node class for the queue
class Node(object):
    def __init__(self, frequency, char_code=None, label=None, value=None):
        # queue data
        self.next = None
        self.prev = None
        self.priority = frequency * -1 

        # char data
        self.frequency = frequency
        self.char_code = char_code
        
        if char_code:
            char = chr(char_code)
            leaf = True
        else:
            char = label
            leaf = False
        
        self.char = char
        self.left = None
        self.right = None
        self.leaf = leaf

    def is_leaf(self):
        return self.leaf
    
    def get_value(self):
        return self.char
    
    def get_value(self):
        return self.char

    def set_value(self, value):
        self.value = value

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right
    
    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None

# priority queue class
class PriQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    # add element to queue
    def enqueue(self, node):

        if self.head is None:
            self.head = node
            self.tail = self.head
        
        else:
            current_node = self.head

            while current_node.next and (node.priority >= current_node.priority):
                current_node = current_node.next
            

            # case 1: one element Head = Tail
            if current_node is self.tail and current_node is self.head:
                if current_node.priority <= node.priority:
                    self.head.next = node
                    node.prev = self.head
                    self.tail = node
                else:
                    node.next = current_node
                    node.prev = None
                    current_node.prev = node
                    current_node.next = None
                    self.head = node
                    self.tail = current_node

            # case 2: if current node is tail 
            elif current_node is self.tail:
                if current_node.priority <= node.priority:
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node

                else:
                    self.tail.prev.next = node
                    node.prev = self.tail.prev
                    node.next = self.tail
                    self.tail.prev = node

            elif current_node is self.head:

                if current_node.priority >= node.priority:
                    node.next = self.head
                    node.prev = None
                    self.head.prev = node
                    self.head = node 

            else:
                current_node.prev.next = node
                node.prev = current_node.prev
                node.next = current_node
                current_node.prev = node

    # remove tail element
    def dequeue(self):
        pop_value = None
        if self.tail:

            if self.tail is self.head:
                pop_value = self.tail               
                self.tail = None
                self.head = None
                return pop_value
            
            pop_value = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        
        return pop_value

    def show_queue(self):
        head=self.head
        print('--------------------------------------------')
        while head is not None:
            print(head.char, head.priority)
            head=head.next
        if self.head:

            print('HEAD:', self.head.char , 'TAIL:', self.tail.char)
            print('--------------------------------------------')
        else:
            print('HEAD:', self.head, 'TAIL:', self.tail)
            print('--------------------------------------------')            

class Tree(object):
    def __init__(self, node=None):
        self.root = node

    def get_root(self):
        return self.root

def pre_order(tree):
    visit_order = list()
    def traverse(node):
        if node:
            # visit the node
            if node.is_leaf():
                visit_order.append((node.get_value(),node.frequency))
            else:
                visit_order.append((node.get_value(),node.frequency))
                # traverse left subtree
                traverse(node.get_left_child())
                # traverse right subtree
                traverse(node.get_right_child())
    
    traverse(tree.get_root())
    
    return visit_order

def path_from_node_to_root(root, char):
    if root is None:
        return None

    elif root.char == char:
        return [char]

    left_answer = path_from_node_to_root(root.left, char)
    if left_answer is not None:
        left_answer.append(root.char)
        return left_answer

    right_answer = path_from_node_to_root(root.right, char)
    if right_answer is not None:
        right_answer.append(root.char)
        return right_answer
    return None


def char_coding(root, char):
    if root is None:
        return None

    elif root.char == char:
        return []

    left_answer = char_coding(root.left, char)
    if left_answer is not None:
        left_answer.append(0)
        return left_answer

    right_answer = char_coding(root.right, char)
    if right_answer is not None:
        right_answer.append(1)
        return right_answer
    
    return None

def huffman_encoding(data):
    freq_dict = calc_string_freq(data)
    prior_queue = PriQueue()

    for item in freq_dict:
        new_node = Node(freq_dict[item], item)
        prior_queue.enqueue(new_node)

    deque_item_1 = prior_queue.dequeue()
    deque_item_2 = prior_queue.dequeue()

    while deque_item_1 and deque_item_2:
        value = deque_item_1.frequency + deque_item_2.frequency
        label = deque_item_1.char + deque_item_2.char
        tree_node = Node(value, label=label)

        if deque_item_1.frequency < deque_item_2.frequency:
            tree_node.left = deque_item_1
            tree_node.right = deque_item_2
        else:
            tree_node.right = deque_item_1
            tree_node.left = deque_item_2
        
        prior_queue.enqueue(tree_node)
        deque_item_1 = prior_queue.dequeue()
        deque_item_2 = prior_queue.dequeue()

    tree_code = Tree(tree_node)
    encode_final = ''
    for char in data:
        list_code = char_coding(tree_code.get_root(), char)
        list_code.reverse()
        encode_final += "".join(str(x) for x in list_code)
    
    return encode_final, tree_code

def huffman_decoding(data_encoded, tree):
    decoded_string = ''
    current_node = tree.get_root()

    for bit in data_encoded:
        if bit == '1':
            current_node = current_node.get_right_child()
        elif bit == '0':
            current_node = current_node.get_left_child()

        if current_node.is_leaf():
            decoded_string += current_node.char
            current_node = tree.get_root()
            continue
        
    return decoded_string

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))



