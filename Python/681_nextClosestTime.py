'''Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits.
There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.'''


class Solution:
    def nextClosestTime(self, time: str) -> str:
        hour, minute = time.split(":")
        nums = sorted(set(hour + minute))
        # print(nums)
        twos = list()
        for i in nums:
            for j in nums:
                twos.append(i + j)
        # print(twos)
        i = twos.index(minute)
        if i + 1 < len(twos) and twos[i + 1] < "60":
            return hour + ":" + twos[i + 1]

        i = twos.index(hour)
        if i + 1 < len(twos) and twos[i + 1] < "24":
            return twos[i + 1] + ":" + twos[0]

        return twos[0] + ":" + twos[0]