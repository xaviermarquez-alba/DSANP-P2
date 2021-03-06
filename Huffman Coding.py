import sys
# calc the frecuency character for a input string, retun a dict
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
            # case 3 if current node is head
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

# encoding char using the binary root
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
    if data is None or data == '':
        print('Invalid input data!')
        return None, None

    freq_dict = calc_string_freq(data)
    prior_queue = PriQueue()

    for item in freq_dict:
        new_node = Node(freq_dict[item], item)
        prior_queue.enqueue(new_node)

    deque_item_1 = prior_queue.dequeue()
    deque_item_2 = prior_queue.dequeue()
    
    # if only 1 item in queue add a aux item to balance the tree with frecuency 0
    if deque_item_2 is None:
        deque_item_2 = Node(0, 1)

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
    if data_encoded is None:
        return None

    decoded_string = ''
    current_node = tree.get_root()

    for bit in data_encoded:
        if not (current_node.left and current_node.right):
            decoded_string += current_node.char
        else:
            if bit == '1':
                current_node = current_node.get_right_child()
            elif bit == '0':
                current_node = current_node.get_left_child()

            if current_node.is_leaf():
                decoded_string += current_node.char
                current_node = tree.get_root()
                continue
        
    return decoded_string


def encode_decode_test(data):
    print("\n")
    if data:
        print ("The content of the data is: {}".format(data))
        print("The size of the data is:{}".format(sys.getsizeof(data)))
    else:
        print ("The content of the data is: None")
        print("The size of the data is: None")

    # encoded data
    encoded_data, tree = huffman_encoding(data)
    
    # decoded data
    decoded_data = huffman_decoding(encoded_data, tree)

    if decoded_data is not None:
        
        print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}".format(encoded_data))
        print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
        print ("The content of the decoded data is: {}".format(decoded_data))


        # if the data is the same after decoded
        if decoded_data == data:
            print('*** Pass Data Test ***')
        else:
            print('*** Fail Data Test ***')
            
        if int(sys.getsizeof(int(encoded_data, base=2))) < int(sys.getsizeof(data)):
            print('*** Pass Compression Size Test ***')
        else:
            print('*** Fail Compression Size Test ***')



if __name__ == "__main__":
    # Tests

    codes = {}
    a_great_sentence = "The bird is the word"
    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}".format(decoded_data))


    # Tests encode and decode
    encode_decode_test("Lorem Ipsum") 
    encode_decode_test("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    encode_decode_test("AAAAAAAAAAAAAAAAAAAA")
    encode_decode_test("B")
    encode_decode_test(' ')
    encode_decode_test('')