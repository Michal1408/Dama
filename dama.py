import PIL
from PIL import Image,ImageDraw
chessboard = []
counter = 0
size_sq = 50
number = 8
width = size_sq * number
height = size_sq * number
col_b =  (0, 0, 0)
col_w = (255, 255, 255)
#
#
#
def createImage():
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    for riadok in range(number):
        for stlpec in range(number):
            x1 = size_sq * stlpec
            y1 = size_sq * riadok
            x2 = x1 + size_sq
            y2 = y1 + size_sq
            if (riadok + stlpec) % 2 == 1:
                color = col_w
            else:
                color = col_b
            draw.rectangle([x1,y1,x2,y2], fill=color)
    #image.save('sachovnica.png')
    image.show()
createImage()
#
#
#
def create_board ():
    global chessboard
    #chessboard = [row] * 8  # mega pruser takto to nikdy nerob !!!!!
    for i in range (8):
        row = [0] * 8
        chessboard.append(row)
#
#
#
def check_it (x, y):
    for i in range (0, 8):
        if chessboard[y][i] == 1:
            return False
        if chessboard[i][x] == 1:
            return False
    for i in range(0,8):    #y
        for o in range(0,8):    #x
            if i+o == x+y:
                if chessboard[i][o] == 1:
                    return False
            if i-o == y-x:
                if chessboard[i][o] == 1:
                    return False
    return True
#
#
#
def queens (n):
    global chessboard , counter
    if n == 8:
        counter += 1
        print(chessboard)
        print(counter)
        print('-----------------------------')
    else:
        for i in range (8):
            if check_it(i,n):
                chessboard[n][i] = 1
                queens(n+1)
                chessboard[n][i] = 0
#
#
#
create_board()
queens(0)
#print(check_it(4,3))