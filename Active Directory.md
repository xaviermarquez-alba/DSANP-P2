# Active Directory
## Data Structure & Time/Space complexity

Similar to "Finding Files", I use a recursive function to travel all groups and search if the user belongs to the current group, calling the function recursively for every subgroup. In the worst-case scenario, the search will take an O (n + m) time, n = number of groups and m = number of users

The space complexity will take O (n) with n = number of groups in the worst case, due to the call stack accumulation.