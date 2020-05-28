import hashlib
import datetime

class Block:
    def __init__(self, data):
        self.timestamp = datetime.datetime.utcnow()
        self.data = data
        self.previous_hash = 0
        self.hash = self.calc_hash()

    def set_previous_hash(self, prev_hash):
        self.previous_hash = prev_hash

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, data):
        new_block = Block(data)

        if self.head is None:
            self.tail = self.head = new_block
        else:
            new_block.set_previous_hash(self.tail.hash)
            self.tail.next = new_block
            self.tail = self.tail.next

new_blockchain = Blockchain()
new_blockchain.add_block('UNO')
new_blockchain.add_block('DOS')
new_blockchain.add_block('TRES')
new_blockchain.add_block('CUATRO')
new_blockchain.add_block('CINCO')
new_blockchain.add_block('SEIS')

print(new_blockchain.head.next.hash)
print(new_blockchain.head.next.next.previous_hash)
print(new_blockchain.tail.hash)