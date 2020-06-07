# array untuk mengecek apakah di suatu row, col, dan box, suatu num sudah terpakai atau belum
isUsedNumInRow = [[False for i in range(10)] for j in range(9)]     # isUsedNumInRow[idxRow][angka]
isUsedNumInCol = [[False for i in range(10)] for j in range(9)]     # isUsedNumInCol[idxRow][angka]
isUsedNumInBox = [[[False for i in range(10)] for j in range(3)] for j in range(3)]     # isUsedNumInBox[X][Y][angka]

# fungsi untuk solve sudokunya
def solveSudoku(board):
    init(board)
    solveRecurr(board) 
    return board

# fungsi solve sudoku dengan rekursi
def solveRecurr(board):
    row, col = findEmptyCell(board)     # mencari empty cell
    if (row==-1): # all filled
        return True
    
    for num in range(1,10): #coba semua angka 1 -> 9
        if (isSafe(num, row, col)):
            assignNum(board, num, row, col)

            if (solveRecurr(board)):    # recurr
                return True

            # if fail, then backtrack
            unassignNum(board, num, row, col)
    
    return False

# fungsi untuk mencari empty cell
def findEmptyCell(board):
    for i in range(9):
        for j in range(9):
            if (board[i][j]==-1):
                return i, j
    return -1, -1

# inisialisasi boardnya
def init(board):
    for i in range(9):
        for j in range(9):
            if (board[i][j]!=-1):
                assignNum(board, board[i][j], i, j)

# fungsi untuk mengecek apakah peletakan num di suatu cell aman/tidak
def isSafe(num, i, j):
    return not((isUsedNumInRow[i][num]) or (isUsedNumInCol[j][num]) or (isUsedNumInBox[i//3][j//3][num]))

# fungsi untuk menaruh num di suatu cell
def assignNum(board, num, i, j):
    board[i][j] = num
    isUsedNumInCol[j][num] = True
    isUsedNumInRow[i][num] = True
    isUsedNumInBox[i//3][j//3][num] = True

# fungsi untuk melepaskan num dari suatu cell
def unassignNum(board, num, i, j):
    board[i][j] = -1
    isUsedNumInCol[j][num] = False
    isUsedNumInRow[i][num] = False
    isUsedNumInBox[i//3][j//3][num] = False