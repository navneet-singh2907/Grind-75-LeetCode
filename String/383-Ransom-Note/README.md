# 383. Ransom Note

## Approach: Hash Map (Frequency Counter)
We store the counts of all characters available in the `magazine` using a hash map. Then, we iterate through the `ransomNote` to verify if the required characters are present in sufficient quantities.

## Complexity Analysis
- **Time Complexity:** $O(m + n)$ — Where $m$ is the length of the magazine and $n$ is the length of the ransom note.
- **Space Complexity:** $O(k)$ — Where $k$ is the number of unique characters (at most 26 for English lowercase letters).
