from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        words = set(wordList)
        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + ch + word[i + 1:]

                    if next_word in words and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, length+1))

        return 0