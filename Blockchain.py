import hashlib
import datetime

class Block(object):
    def __init__(self, data):
        self.timestamp = datetime.datetime.utcnow()
        self.data = str(data)
        self.previous_hash = 0
        self.hash = self.calc_hash()
        self.next = None

    def set_previous_hash(self, prev_hash):
        self.previous_hash = prev_hash

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def add_block(self, data):
        if data is None:
            print('Invalid data not added to the Blockchain')
            return
        
        new_block = Block(data)

        if self.head is None:
            self.head = new_block
            self.tail = self.head 
        else:
            new_block.set_previous_hash(self.tail.hash)
            self.tail.next = new_block
            self.tail = new_block

def test_blockchain(blockchain_list):
    pass_test = True 
    blockchain = Blockchain()
    for block in blockchain_list:
        blockchain.add_block(block)
    
    # show block chain
    current_node = blockchain.get_head()

    print('--------------------BLOCKCHAIN NODES--------------------')
    while current_node:
        print("Data: " + current_node.data + " | Timestamp: " + str(current_node.timestamp))
        print("Hash: " + current_node.hash)
        print("Prev Hash: " + str(current_node.previous_hash))
        print('--+--')
        
        # test if prevhash
        if not current_node is blockchain.get_head() and current_node.next:
            if not current_node.hash == current_node.next.previous_hash:
                pass_test = False
            
        current_node = current_node.next
    print('--------------------BLOCKCHAIN END--------------------')

    if pass_test:
        print('*** Test Pass! ****')
    else:
        print('*** Test Fail! ****')
    print("\n")

# Test 1
test_blockchain(['ABCW', 'CDGR', 'JYEBA']) 

# Test 2
test_blockchain([1,2,3,4]) 

# Test 3
test_blockchain(['#One Item!'])

# Test 4
test_blockchain(['', 'test', 'empty', 'string']) # empty string is a valid item for the blockchain

# Test 5
test_blockchain(['A', 'B', None, 'C', None, 'D']) # expected output: blockchain ignoring None items and  print 2 'Invalid data!', 