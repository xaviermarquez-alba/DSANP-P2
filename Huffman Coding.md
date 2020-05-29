# Huffman Coding
## Data Structure & Time/Space complexity

For this problem, I used a Binary tree, priority queue and a dictionary

Dictionary is used to store the characters and his frequency, the character ascii code is used as dict key. The Priority queue + Tree is used for the Huffman algorithm process

Encoding:
First, we create a frequency char dict this is O (n), n = number of chars.
second, we add every item to a priority queue, this is a O (m) with m = numbers of unique chars on the data.
The enqueue process is based on the node priority in the worst-case scenario we need to travel all nodes for every new node added so this is O (n * log (n)) time complexity

To build a huffman tree, we need to dequeue two items and add one for every item on the queue, so this is O (n) to dequeue all items and O (n / 2) to add one every two dequeue.

Encoding the data for every char is O (n) time complexity, n = number of chars


Decoding:
To decode the time complexity is O (n) to convert all bits on characters using the binary tree.

For the space complexity, 
the frequency dict is O (n), n = number of unique characters
the priority queue is O (n), n = number of unique characters
the binary tree is composed by the queue nodes so no extra spaced is required in this case and also  every two nodes one new node is created this is O (n / 2)

