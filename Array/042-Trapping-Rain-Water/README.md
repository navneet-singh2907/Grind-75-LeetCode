# 042. Trapping Rain Water

## Approach: Two Pointers
We use two pointers to converge from the ends toward the center. By tracking the maximum height encountered from both sides, we can calculate the water trapped at each step. Since water is limited by the shorter wall, we always move the pointer with the smaller maximum height.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We visit each element once.
- **Space Complexity:** $O(1)$ — Only a few integer variables are used.
