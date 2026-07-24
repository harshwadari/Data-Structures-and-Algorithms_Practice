# 93. Restore IP Addresses
"""
A valid IP address consists of exactly four integers separated by single dots. 
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", 
"192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be 
formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You 
may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

1 <= s.length <= 20
s consists of digits only.
"""

#Optimal Approach using Recursion Backtracking 
# TC = O(3^N) and SC = O(N) stack space where n is lenght of given string
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        if len(s) < 4 or len(s) > 12:
            return []
        def backtrack(index,subset):
            if len(subset) == 4:
                if index == len(s):
                    result.append(".".join(subset))
                return
            for i in range(1,4):
                if index + i > len(s):
                    break
                part = s[index:index+i]
                if len(part) > 1 and part[0] == '0':
                    continue
                if int(part) > 255:
                    continue
                subset.append(part)
                backtrack(index + i,subset)
                subset.pop()
        backtrack(0,[])
        return  result