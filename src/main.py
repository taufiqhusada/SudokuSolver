from solver import solveSudoku
from boardOcr import boardImgToMatrix
from utilPrint import printResultToFile, printResultToTerminal
import time

# inisialisasi
board = [[-1 for i in range(9)] for j in range(9)]
typeInput = int(input("masukkan pilihan input (1: text file, 2: image): "))
fileName = ""

# jika input berupa file txt
if (typeInput==1):
    # read file
    fileName = input("masukkan nama file input ('<name>.txt'): ")
    f = open("../test/" + fileName + ".txt", "r")
    inputLines = f.readlines()
    f.close()
    
    # create board based on input
    for i in range(9):
        thisLine = inputLines[i].rstrip('\n').split(" ")
        for j in range(9):
            if (thisLine[j]!='#'):
                board[i][j] = ord(thisLine[j]) - ord('0') 
    
    # print board awal
    print("board awal:")
    for i in range(9):
        print(board[i])

# jika input berupa file image (png)
else:   
    # read file image
    fileName = input("masukkan nama file image ('<nama>.png'): ")
    mat = boardImgToMatrix("../test/" + fileName + ".png")
    for i in range(9):
        for j in range(9):
            if (mat[i][j]!=''):
                board[i][j] = ord(mat[i][j]) - ord('0') 
    
    # print board awal
    print("board awal:")
    for i in range(9):
        print(board[i])

# solve (catat waktunya juga)
startTime = time.time()
solveSudoku(board)
endTime = time.time()

# print result
print("\nsolved in " + str(endTime-startTime) + " secs")
printResultToTerminal(board)
printResultToFile(board, fileName)



