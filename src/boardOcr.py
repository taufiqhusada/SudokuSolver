import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'../bin/Tesseract-OCR/tesseract.exe'

# fungsi untuk mengconvert 1 cell menjadi 1 angka
def processCell(imgBoard, i, j, boardHeight, boardWidth):
    top = (boardHeight/9)*i + 3
    bottom = (boardHeight/9)*(i+1) - 3
    left = (boardWidth/9)*j + 4
    right = (boardWidth/9)*(j+1) - 3
    
    cell = imgBoard.crop((left, top, right, bottom))
    return pytesseract.image_to_string(cell, config='--psm 6')

# fungsi untuk mengubah image board menjadi matrix of char yang bersesuaian 
def boardImgToMatrix(imgBoardPath):
    matrix = [[-1 for i in range(9)] for j in range(9)]
    imgBoard = Image.open(imgBoardPath)
    
    boardWidth, boardHeight = imgBoard.size

    for i in range(9):
        for j in range(9):
            num = processCell(imgBoard, i, j, boardHeight, boardWidth)
            matrix[i][j] = num
    
    # melihat hasil ocr
    print(matrix)
    return matrix

# boardImgToMatrix("../test/image1.png")