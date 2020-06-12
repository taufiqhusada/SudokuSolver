# fungsi untuk print result ke terminal
def printResultToTerminal(board):
    for i in range(9):
        if (i%3==0 and i>0):
            for j in range(11):
                print("- ", end="")
            print()
        print(convertLine(board,i))        

    # print letak 5
    letakAll5 = findAll5(board)
    print("\nLetak angka 5:")
    for e in letakAll5:
        print("( " + str(e[0]) + " , " + str(e[1]) + " )")

# fungsi untuk print result ke file
def printResultToFile(board, fileName):
    f = open("../result/result_" + fileName, "w")
    for i in range(9):
        if (i%3==0 and i>0):
            for j in range(11):
                f.write("- ")
            f.write("\n")
        f.write(convertLine(board,i) + "\n")
    
    # print letak 5
    f.write("\nLetak angka 5:\n")
    letakAll5 = findAll5(board)
    for e in letakAll5:
        f.write("( " + str(e[0]) + " , " + str(e[1]) + " )\n")

    f.close()

# fungsi untuk mencari koordinat angka 5
def findAll5(board):
    res = []
    for i in range(9):
        for j in range(9):
            if (board[i][j]==5):
                res.append((i+1,j+1))
    return res

def convertLine(board, i):
    line = ""
    for j in range(9):
        line += (str(board[i][j]))
        line += (" ")
        if (j%3==2 and j<8):
            line += ("| ")
    return line

