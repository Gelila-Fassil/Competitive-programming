from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        predecessors = defaultdict(list)
        distance = {beginWord: 0}
        queue = deque([beginWord])
        found = False
        while queue and not found:
            layer_size = len(queue)
            visited_this_layer = {}
            
            for _ in range(layer_size):
                curr_word = queue.popleft()
                for i in range(len(curr_word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = curr_word[:i] + char + curr_word[i+1:]
                        
                        if next_word in wordSet:
                            if next_word not in distance or distance[next_word] == distance[curr_word] + 1:
                                if next_word not in distance:
                                    distance[next_word] = distance[curr_word] + 1
                                    queue.append(next_word)
                                
                                predecessors[next_word].append(curr_word)
                                
                                if next_word == endWord:
                                    found = True
        results = []
        def backtrack(word, path):
            if word == beginWord:
                results.append(path[::-1])
                return
            for parent in predecessors[word]:
                path.append(parent)
                backtrack(parent, path)
                path.pop()
        
        if found:
            backtrack(endWord, [endWord])
        return results