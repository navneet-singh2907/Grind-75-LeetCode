Approach: One-Pass Hash Map. Instead of checking every pair (Brute Force), I have used a dictionary to store the numbers we've already seen. 
This turns a $O(n^2)$ search into a $O(n)$ lookup.
Complexity:Time: 
$O(n)$ — I traverse the list only once. 
$O(n)$ — In the worst case, we store every element in the hash map.
