'''Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.'''

import collections


class Solution:
    def compress(self, chars: List[str]) -> int:
        count = collections.Counter(chars)
        i = j = 0

        for c, each in enumerate(chars):
            if c + 1 == len(chars) or chars[c + 1] != each:
                chars[j] = chars[i]
                j += 1
                if c > i:
                    num = str(c - i + 1)
                    for d in num:
                        chars[j] = d
                        j += 1
                i = c + 1
        return j