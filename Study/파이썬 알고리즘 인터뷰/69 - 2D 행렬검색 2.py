# 첫 행의 맨 뒤에서 탐색
def searchMatrix(matrix, target):
    # 예외처리
    if not matrix:
        return False
    
    # 첫행의 맨뒤
    row = 0
    col = len(matrix[0]) - 1
    
    while row <= len(matrix) - 1 and col >= 0:  #row가 입력된 행보다 작고 열이 0보다 크다면 반복문
        if target == matrix[row][col]:
            return True
        # 타겟이 작으면 왼쪽으로 이동
        elif target < matrix[row][col]:
            col -=1
        elif target > matrix[row][col]:
            row +=1
    return False

#파이썬다운 방식
def anysearchMatrix(matrix, target):
    return any(target in row for row in matrix)

array = [
    [1,4,7,11,15]
    [2,5,8,12,19]
    [3,6,9,16,22]
    [10,13,14,17,24]
    [18,21,23,26,30]
]
