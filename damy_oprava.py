import os
from PIL import Image, ImageDraw

chessboard = []
counter = 0
size_sq = 50
number = 8
width = size_sq * number
height = size_sq * number
col_b = (0, 0, 0)
col_w = (255, 255, 255)

# priecinok, kde je tento skript (queen.png musi byt tu)
zlozka_skriptu = os.path.dirname(os.path.abspath(__file__))

# priecinok, kam sa ulozia obrazky (vytvori sa vedla skriptu)
folder = os.path.join(zlozka_skriptu, 'sachovnice')
os.makedirs(folder, exist_ok=True)

# nacitaj obrazok damy a zmensi ho na velkost policka
queen_img = Image.open(os.path.join(zlozka_skriptu, 'queen.png')).convert('RGBA')
queen_img = queen_img.resize((size_sq, size_sq))

#
#
#
def createImage(board, cislo):
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
            draw.rectangle([x1, y1, x2, y2], fill=color)

            # ak je na policku dama, vloz obrazok queen.png
            if board[riadok][stlpec] == 1:
                image.paste(queen_img, (x1, y1), queen_img)

    # kazde riesenie ma iny nazov: sachovnica_1.png ... sachovnica_92.png
    image.save(os.path.join(folder, f'sachovnica_{cislo}.png'))


#
#
#
def create_board():
    global chessboard
    # chessboard = [row] * 8  # mega pruser takto to nikdy nerob !!!!!
    for i in range(8):
        row = [0] * 8
        chessboard.append(row)


#
#
#
def check_it(x, y):
    for i in range(0, 8):
        if chessboard[y][i] == 1:
            return False
        if chessboard[i][x] == 1:
            return False
    for i in range(0, 8):    # y
        for o in range(0, 8):    # x
            if i + o == x + y:
                if chessboard[i][o] == 1:
                    return False
            if i - o == y - x:
                if chessboard[i][o] == 1:
                    return False
    return True


#
#
#
def queens(n):
    global chessboard, counter
    if n == 8:
        counter += 1
        print(chessboard)
        print(counter)
        print('-----------------------------')
        createImage(chessboard, counter)   # nakresli a uloz toto riesenie
    else:
        for i in range(8):
            if check_it(i, n):
                chessboard[n][i] = 1
                queens(n + 1)
                chessboard[n][i] = 0


#
#
#
create_board()
queens(0)