'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ''
        if len(strs) == 0:
            exit
        elif len(strs) == 1:
            result = strs[0]
        else:
            i = 1
            elem = strs[0][:i]

            flag = True
            while True:
                for each in strs:
                    if len(elem) > len(each):
                        flag = False
                        break
                    if each[:i] != elem:
                        flag = False
                        break
                if flag == True:
                    result = elem
                    i += 1
                    elem = strs[0][:i]
                    if i > len(strs[0]):
                        break
                else:
                    break
        return result
