import pytesseract
from PIL import Image
import os.path
import os
pytesseract.pytesseract.tesseract_cmd = r'../bin/Tesseract-OCR/tesseract.exe'

# fungsi untuk mengconvert 1 cell menjadi 1 angka
def processCell(fileName, imgBoard, i, j, boardHeight, boardWidth):
    croppedFilePath = "../test/" + fileName + "/" + fileName + "_" + str(i) + "_" + str(j)+".png"
    
    # find cropped image cell, if already exist
    if (os.path.exists(croppedFilePath)):
        croppedImg = Image.open(croppedFilePath)
        return pytesseract.image_to_string(croppedImg, config='--psm 6')
    else: #if not exist then crop image then save it
        top = (boardHeight/9)*i + 3
        bottom = (boardHeight/9)*(i+1) - 3
        left = (boardWidth/9)*j + 4
        right = (boardWidth/9)*(j+1) - 3
        
        croppedImg = imgBoard.crop((left, top, right, bottom))
        
        # check if folder not exist then create it
        if (not (os.path.exists("../test/" + fileName))):
            os.makedirs("../test/" + fileName)
        croppedImg.save(croppedFilePath,'PNG')
        return pytesseract.image_to_string(croppedImg, config='--psm 6')

# fungsi untuk mengubah image board menjadi matrix of char yang bersesuaian 
def boardImgToMatrix(fileName):
    matrix = [[-1 for i in range(9)] for j in range(9)]
    imgBoard = Image.open("../test/" + fileName + ".png")
    
    boardWidth, boardHeight = imgBoard.size

    for i in range(9):
        for j in range(9):
            num = processCell(fileName, imgBoard, i, j, boardHeight, boardWidth)
            matrix[i][j] = num
    
    # melihat hasil ocr
    print(matrix)
    return matrix
