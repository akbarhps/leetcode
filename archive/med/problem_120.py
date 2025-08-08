from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cached = []

        for i, listval in enumerate(triangle):
            tempcache = []
            for j, item in enumerate(listval):
                if i == 0:
                    tempcache.append(item)
                else:
                    min1, min2 = 100000, 100000
                    if j - 1 >= 0:
                        min1 = item + cached[i - 1][j-1]
                    if j < len(cached[i-1]):
                        min2 = item + cached[i - 1][j]
                    tempcache.append(min(min1, min2))

            cached.append(tempcache)
            
        return min(cached[len(cached) - 1])


# triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
# triangle = [[-10]]
# triangle = [[-1],[2,3],[1,-1,-3]]
triangle = [   [2], 
              [3, 4],
             [6, 5, 9], 
            [4, 4, 8, 0]]
    
print(Solution().minimumTotal(triangle))
