def spiralOrder(matrix):
    output = []
    rowindex = 0
    colindex = 0
    rowlen = len(matrix) - 1
    collen = len(matrix[0]) - 1
    min_val = 0

    order = 0
    while len(output) < (len(matrix) * len(matrix[0])):
        output.append(matrix[rowindex][colindex])

        if order == 0:
            if colindex >= collen: order += 1
        elif order == 1:
            if rowindex >= rowlen: order += 1
        elif order == 2:
            if colindex <= min_val:
                order += 1
                min_val += 1
        elif order == 3:
            if rowindex <= min_val:
                order += 1
                rowlen -= 1
                collen -= 1
                
        order %= 4

        if order == 0:
            colindex += 1
        elif order == 1:
            rowindex += 1
        elif order == 2:
            colindex -= 1
        elif order == 3:
            rowindex -= 1

    return output


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))
