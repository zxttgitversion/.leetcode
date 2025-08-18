#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        is_prime = [True] * n 
        is_prime[0] = is_prime[1] = False

        import math
        limit = int(math.sqrt(n))
        for i in range(2, limit + 1):
            if not is_prime[i]:
                continue
            for j in range(i * i, n, i):
                is_prime[j] = False

        return sum(is_prime)
  
        
# @lc code=end

