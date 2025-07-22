class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        output = ['' for _ in range(0, numRows)]

        dir = 0
        index = 0
        for i, char in enumerate(s):
            if (dir > 0 and index == 0) or index == numRows - 1:
                dir += 1

            print(i, index, char)
            output[index] += char
            
            if dir % 2 == 0:
                index += 1
            else:
                index -= 1

        return ''.join(output)


s = "ABC"
numRows = 1
print(Solution().convert(s, numRows))
