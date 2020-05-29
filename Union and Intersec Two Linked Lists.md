# Union and Intersection of Two Linked Lists
## Data Structure & Time/Space complexity

The data structure required for this problem is two Linked lists, in addition, I used sets to remove duplicated items.

Union: the function travel both list and add the item to a set, this is a O(n + m) time complexity, with n=lenght of list 1 and m=lenght of list 2
For the space complexity in the worst-case scenario the lists have no intersection so we need to store all items, O(n + m)

intersection: for the intersection the function store list 1 on a set, then check for every item in list 2 for the intersection, in the worst-case scenario the set "in" operation is O(n), so the final time complexity worst case is O(n * m), m = length list 1  and n = length list 2.
The space complexity in the worst-case scenario is O(n) with list 1 = list 2, we use two linked list and one set of n elements.