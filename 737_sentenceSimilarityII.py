'''Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs,
determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar,
if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar,
then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar,
even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"]
can never be similar to words2 = ["doubleplus","good"].'''


import collections

class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        pairsDict = collections.defaultdict(set)
        for first, second in pairs:
            pairsDict[first].add(second)
            pairsDict[second].add(first)

        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            else:
                stack = [words1[i]]
                visited = set()
                flag = False
                while stack:
                    curr = stack.pop()
                    if curr == words2[i]:
                        flag = True
                        break
                    for each in pairsDict[curr]:
                        if each not in visited:
                            visited.add(each)
                            stack.append(each)
                if not flag:
                    return False
        return True