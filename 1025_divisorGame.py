'''Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.'''


class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        alice = False
        count = 0
        flag = False
        while N > 1:
            for num in range(1, N):
                if (N % num) == 0:
                    N = N - num
                    flag = True
                    break
            if count % 2 == 0:
                alice = True
            else:
                if flag:
                    alice = False
            count += 1
        return alice
