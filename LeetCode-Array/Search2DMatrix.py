

def search(matrix, target):
    row = len(matrix)-1
    col = 0
    while row >=0 and col <len(matrix[0]):
        if target > matrix[row][col]:
            col+=1
        elif target < matrix[row][col]:
            row-=1
        else:
            return [row, col]
