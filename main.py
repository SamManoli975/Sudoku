import pygame as pg
import sys

pg.init()
size = (750, 750)  # Width, Height
screen = pg.display.set_mode(size)
font = pg.font.SysFont('none', 80)
font2 = pg.font.SysFont('none', 50)
pg.display.set_caption("My pygame Window")
screen.fill((255,255,255))

x=0
y=0
val = 0
diff = 720 / 9#this is a test change to commitsss


number_grid = [
    [0, 0, 0, 5, 0, 0, 8, 0, 0],
    [0, 2, 9, 0, 7, 4, 0, 3, 0],
    [3, 1, 0, 0, 9, 0, 0, 4, 6],
    [7, 5, 1, 0, 0, 3, 0, 0, 4],
    [2, 0, 0, 0, 0, 0, 0, 0, 9],
    [4, 0, 0, 7, 0, 0, 3, 1, 8],
    [1, 8, 0, 0, 2, 0, 0, 6, 7],
    [0, 6, 0, 8, 1, 0, 4, 5, 0],
    [0, 0, 7, 0, 0, 9, 0, 0, 0],
]

solve_number_grid = [row[:] for row in number_grid]
# solve_number_grid = number_grid[:]
# print(solve_number_grid)
# target_number = 9
# for row_index, row in enumerate(number_grid):
#     for col_index, number in enumerate(row):
#         if number == target_number:
#             print(f"Number {target_number} found at row {row_index + 1}, column {col_index + 1}")
# print(number_grid[0][5])

def draw():
    
    for i in range(0,10):#looping through from 0-9
        line_width = 10 if i%3 == 0 else 3#changing line width to clearly show the 9 squares 
        #drawing lines
        pg.draw.line(screen,(0,0,0), ((80*i)+15,15),((80*i)+15,735),line_width)
        pg.draw.line(screen,(0,0,0), (15,(80*i)+15),(735,(80*i)+15),line_width)

        # pg.draw.lines(screen, (255,255,255), False, (80,0),(80,720), 3)



def get_cord(pos):
       global x
       x = (pos[0]-15)//diff
       global y
       y = (pos[1]-15)//diff

def clickBox():  
    draw()
    print('yeah')
    # click = pg.mouse.get_pressed()
    if pg.mouse.get_pressed()[0]:  # Check if the left mouse button is pressed
        print('clicked')
        print(pg.mouse.get_pos())
        for i in range(2): #(x * diff)+15, (y * diff)+15, diff, diff
            pg.draw.line(screen, (255, 0, 0), ((x * diff - 1) + 15, (y + i) * diff + 15), (x * diff + diff + 1 + 15, (y + i) * diff + 15), 3)
            pg.draw.line(screen, (255, 0, 0), ((x + i) * diff + 15, y * diff + 15), ((x + i) * diff + 15, y * diff + diff + 15), 3)
    
            # screen.fill((0,0,0))
            
            
                

                
           
        # if pos[0] in range(0,80) and pos[1] in range(0,80):
            
        #     
        # elif pos[0] in range(80,160) and pos[1] in range(0,80):
        #     print("Box 2 clicked")




        
draw()
def draw_numbers():
    row = 0
    offset = 35
    while row < 9:
    
        col = 0
        while col < 9:
            number = number_grid[row][col]
            if number != 0 :

                # text_rect = text.get_rect()
                text = font.render(str(number), True, (0,0,0))
                # text_rect.center = ((col*80)+40, (row*80)+40)
                screen.blit(text, ((col*80) + offset+5, (row*80) + offset-2))
            
            col +=1
        row +=1

#function to enter a value
def draw_val(val):
    grid_x = int(x)
    grid_y = int(y)
    # print('these are the grid coords',grid_x,grid_y)
    #debugging
    # grid_x = int(x // diff)
    # grid_y = int(y // diff)
    # print('the number in this cell is ',number_grid[grid_y][grid_x])
    # print(grid_y,grid_x)
    if number_grid[grid_y][grid_x] == 0:
        print('this square is empty')
        pg.draw.rect(screen, (255,255,255), ((x * diff+6)+15, (y * diff+6)+15, diff-13, diff-13))

        text1 = font2.render(str(val), 1, (0, 0, 255))
        screen.blit(text1, (x * diff+40, y * diff+40))

#function to check if the value works for the sudoky board,
#so that there is not the same number in the 3x3 square or in the row or column
def valid(grid, y, x, val):
    x = int(x)
    y = int(y)

    # Check row
    row = grid[x]
    if val in row:
        return False

    # Check column
    col = [grid[i][y] for i in range(9)]
    if val in col:
        return False

    # Check 3x3 box
    box_x = x // 3 * 3
    box_y = y // 3 * 3
    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if grid[i][j] == val:
                return False

    # Return True if the number is valid, False if it isn't
    return True




# mouse_clicked = False
validNum = False
run = True
while run == True:
    for event in pg.event.get():  
        if event.type == pg.QUIT:
           run = False
           pg.quit()  
           sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            get_cord(pg.mouse.get_pos())
            # mouse_clicked = True
            clickBox()
            pg.display.flip()
            pg.time.delay(50)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pg.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pg.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pg.K_DOWN:
                y+= 1
                flag1 = 1
            if event.key == pg.K_1:
                val = 1
            if event.key == pg.K_2:
                val = 2
            if event.key == pg.K_3:
                val = 3
            if event.key == pg.K_4:
                val = 4
            if event.key == pg.K_5:
                val = 5
            if event.key == pg.K_6:
                val = 6
            if event.key == pg.K_7:
                val = 7
            if event.key == pg.K_8:
                val = 8
            if event.key == pg.K_9:
                val = 9
            
    
            if val != 0:
                # get_cord(pg.mouse.get_pos())
                
                
                if valid(solve_number_grid,x,y,val) == True:
                    solve_number_grid[int(y)][int(x)] = val
                    validNum = True
                    print('it works')
                if validNum == True:
                    draw_val(val)
                    validNum = False
                # pg.display.flip()
                val = 0
                # pg.time.delay(50)
                # mouse_clicked = False

    

    
    draw_numbers()#this is the function to draw the numbers he
    pg.display.flip()





    