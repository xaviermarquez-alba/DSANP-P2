# Least Recently Used Cache
## Data Structure & Time/Space complexity

Data structure used: Doubly Linked list + Dictionary

Doubly Linked list is used to manage the cache capacity using the last recent entry. The doubly linked list permits insert and remove items on 0 (1) time.

The Dictionary is the cache selected for fast lookup on O(1) time. Every new entry is added to the dict and the priority in the list is updated, using the node as reference.

The space complexity will be determined by the capacity of the cache O(c)