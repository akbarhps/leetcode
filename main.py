from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0: return -1
        datalen = len(gas)

        startindex = 0
        index = startindex + 1
        curgas = gas[startindex]
        while True:
            index %= datalen
            if index == startindex: break
            
            g = gas[index]
            c = cost[index - 1]
            if curgas - c < 0:
                startindex = (startindex + 1) % datalen
                index = startindex + 1
                curgas = gas[startindex]
            else:
                curgas += g
            
            index += 1
            
        return startindex


# gas = [1, 2, 3, 4, 5]
# cost = [3, 4, 5, 1, 2]
# gas = [5, 1, 2, 3, 4]
# cost = [4, 4, 1, 5, 1]
# gas = [2, 3, 4]
# cost = [3, 4, 3]
# gas = [5, 8, 2, 8]
# cost = [6, 5, 6, 6]

gas = [5,5,1,3,4]
cost = [8,1,7,1,1]
print(Solution().canCompleteCircuit(gas, cost))
