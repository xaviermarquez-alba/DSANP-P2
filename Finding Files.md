# Finding Files
## Data Structure & Time/Space complexity

For this problem I use a recursive function to travel all nested directories and find the files match with the suffix required, calling the function recursively for every directory in the worst case will take an O(n + m) time, n = number of directories and m = number of files because we also need to check each file.

using recursion generally will require more space than a normal function
the amount of space used is determined by the call stack, in the worst case the function is called for every directory with nested directories, this is a 0(n) space complexity, n = number of total directories.