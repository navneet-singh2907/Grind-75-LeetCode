from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        
        # Pre-process wordList into pattern groups
        # e.g., "h*t": ["hot", "hit"]
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        
        # BFS Queue: (current_word, level)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            current_word, level = queue.popleft()
            
            for i in range(L):
                # Check all possible patterns for the current word
                pattern = current_word[:i] + "*" + current_word[i+1:]
                
                # Visit all words that match this pattern
                for neighbor in all_combo_dict[pattern]:
                    if neighbor == endWord:
                        return level + 1
                    
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                
                # Clear the pattern list to avoid redundant work
                all_combo_dict[pattern] = []
                
        return 0
