'''There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of
this new language. Derive the order of letters in this language.'''

import collections

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = dict()
        letters = [-1 for i in range(26)]
        for i in range(len(words)):
            for j in range(len(words[i])):
                key = ord(words[i][j]) - ord('a')
                letters[key] = 0
                graph[key] = set()

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            i = 0
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    key1 = ord(word1[j]) - ord('a')
                    key2 = ord(word2[j]) - ord('a')
                    level = letters[key2]
                    if key2 not in graph[key1]:
                        letters[key2] = level + 1
                        graph[key1].add(key2)
                    break

        queue = collections.deque()
        result = ''
        for i in range(26):
            if letters[i] == 0:
                queue.appendleft(i)

        while queue:
            curr = queue.popleft()
            result += chr(curr + ord('a'))

            for ch in graph[curr]:
                letters[ch] -= 1
                if letters[ch] == 0:
                    queue.append(ch)

        return result if len(graph) == len(result) else ''
