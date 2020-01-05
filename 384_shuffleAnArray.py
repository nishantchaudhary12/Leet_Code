'''Shuffle a set of numbers without duplicates.'''


class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.arr

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        curr = list(self.arr)
        for i in range(len(curr)):
            j = random.randrange(0, len(curr))
            curr[i], curr[j] = curr[j], curr[i]
        return curr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()