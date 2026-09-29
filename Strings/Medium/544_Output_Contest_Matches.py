# 544. Output Contest Matches
"""
During the NBA playoffs, we always set the rather strong team to play with the rather weak team, like making the rank 1 team play with the rank nth team, which is a good strategy to make the contest more interesting.

Given n teams, return their final contest matches in the form of a string.

The n teams are labeled from 1 to n, which represents their initial rank (i.e., Rank 1 is the strongest team and Rank n is the weakest team).

We will use parentheses '(', and ')' and commas ',' to represent the contest team pairing. We use the parentheses for pairing and the commas for partition. During the pairing process in each round, you always need to follow the strategy of making the rather strong one pair with the rather weak one.

Example 1:
Example 1:

Input: n == 4 

Output: "((1,4),(2,3))"

Explanation:

In the first round, we pair the team 1 and 4, the teams 2 and 3 together, as we need to make the strong team and weak team together.

And we got (1, 4),(2, 3).

In the second round, the winners of (1, 4) and (2, 3) need to play again to generate the final winner, so you need to add the paratheses outside them.

And we got the final answer ((1,4),(2,3)).

Example 2:
Example 2:

Input: n == 8 

Output: "(((1,8),(4,5)),((2,7),(3,6)))"

Explanation:

First round: (1, 8),(2, 7),(3, 6),(4, 5)
Second round: ((1, 8),(4, 5)),((2, 7),(3, 6))
Third round: (((1, 8),(4, 5)),((2, 7),(3, 6)))
Since the third round will generate the final winner, you need to output the answer (((1,8),(4,5)),((2,7),(3,6))).

Now Your Turn!
Pick the correct output for the given input
Example 3 :

Input n == 16 


“((((1,16),(8,9)),((4,13),(5,12))),(((2,15),(7,10)),((3,14),(6,11))))”

((((3,10),(5,6)),((2,15),(4,13))),(((1,16),(7,9)),((8,14),(11,12))))

((((2,14),(6,9)),((5,16),(7,13))),(((1,15),(4,10)),((3,8),(11,12))))

((((4,11),(7,8)),((3,10),(5,13))),(((1,14),(2,16)),((9,15),(6,12))))
Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

Constraints:
n == 2x where x in in the range [1, 12].
"""

# Optimal appraoch using recursion 
# TC = O(N) and SC = O(N)
class Solution:
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Your code goes here
        team = [str(i) for i in range(1,n+1)]
        def recursion(team):
            if len(team) == 1:
                return team[0]
            ans = []
            left = 0
            right =  len(team) - 1
            while left < right:
                match = "(" + team[left] + "," + team[right] + ")"
                ans.append(match)
                left += 1
                right -= 1
            return recursion(ans)
        return recursion(team)



