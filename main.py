import pygame as pg
import sys

pg.init()
size = (750, 750)  # Width, Height
screen = pg.display.set_mode(size)
font = pg.font.SysFont('none', 80)
font2 = pg.font.SysFont('none', 70)
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
#debugging with a test grid
#     [0, 0, 4, 5, 3, 1, 8, 9, 2],
#     [8, 2, 9, 6, 7, 4, 1, 3, 5],
#     [3, 1, 5, 2, 9, 8, 7, 4, 6],
#     [7, 5, 1, 0, 0, 3, 6, 2, 4],
#     [2, 3, 8, 0, 0, 6, 5, 7, 9],
#     [4, 9, 6, 7, 0, 2, 3, 1, 8],
#     [1, 8, 3, 0, 2, 5, 9, 6, 7],
#     [9, 6, 2, 8, 1, 0, 4, 5, 3],
#     [5, 4, 7, 0, 0, 9, 2, 8, 1],

#creating a copy of the grid
solve_number_grid = [row[:] for row in number_grid]

# testing copying the grid
# solve_number_grid = number_grid[:]

#testing 
# target_number = 9
# for row_index, row in enumerate(number_grid):
#     for col_index, number in enumerate(row):
#         if number == target_number:
#             print(f"Number {target_number} found at row {row_index + 1}, column {col_index + 1}")
# print(number_grid[0][5])


#functino to draw the lines of the sudoku grid
def draw():
    
    for i in range(0,10):#looping through from 0-9
        line_width = 10 if i%3 == 0 else 3#changing line width to clearly show the 9 squares 
        #drawing lines
        pg.draw.line(screen,(0,0,0), ((80*i)+15,15),((80*i)+15,735),line_width)
        pg.draw.line(screen,(0,0,0), (15,(80*i)+15),(735,(80*i)+15),line_width)

        # pg.draw.lines(screen, (255,255,255), False, (80,0),(80,720), 3)


#function to get the coords of the mouse 
def get_cord(pos):
       global x
       x = (pos[0]-15)//diff
       global y
       y = (pos[1]-15)//diff

def clickBox(x, y):
    draw()

    # Check if the left mouse button is pressed
    mouse_clicked = pg.mouse.get_pressed()[0]
    
    # Check if the mouse click occurred within the current box
    mouse_pos = pg.mouse.get_pos()
    if (15 + x * diff) <= mouse_pos[0] <= (15 + (x + 1) * diff) and (15 + y * diff) <= mouse_pos[1] <= (15 + (y + 1) * diff):
        highlight_box(x, y, mouse_clicked)

    # If called from arrow key press, highlight the box in the specified direction
    else:
        if pg.key.get_pressed()[pg.K_LEFT]:
            highlight_box(x, y, False)
        elif pg.key.get_pressed()[pg.K_RIGHT]:
            highlight_box(x, y, False)
        elif pg.key.get_pressed()[pg.K_UP]:
            highlight_box(x, y, False)
        elif pg.key.get_pressed()[pg.K_DOWN]:
            highlight_box(x, y, False)

def highlight_box(x, y, mouse_clicked):
    if mouse_clicked:
        for i in range(2):
            pg.draw.line(screen, (255, 0, 0), ((x * diff - 1) + 15, (y + i) * diff + 15), (x * diff + diff + 1 + 15, (y + i) * diff + 15), 3)
            pg.draw.line(screen, (255, 0, 0), ((x + i) * diff + 15, y * diff + 15), ((x + i) * diff + 15, y * diff + diff + 15), 3)
        print(f'Clicked on box ({x}, {y})')
    else:
        for i in range(2):
            pg.draw.line(screen, (255, 0, 0), ((x * diff - 1) + 15, (y + i) * diff + 15), (x * diff + diff + 1 + 15, (y + i) * diff + 15), 3)
            pg.draw.line(screen, (255, 0, 0), ((x + i) * diff + 15, y * diff + 15), ((x + i) * diff + 15, y * diff + diff + 15), 3)



#function to solve the sudoku puzzle using backtracking
# so it will go through the grid and check if the number is valid, if it isnt it will go back and change the number
# def solve(grid, r, c):
#     if r == 9:
#         return True
#     elif c == 9:
#         # Move to the next row first, then reset the column index to 0
#         return solve(grid, r + 1, 0)
#     elif grid[r][c] != 0:
#         return solve(grid, r, c + 1)
#     else:
#         for k in range(1, 10):
#             if valid(grid, r, c, k):
#                 grid[r][c] = k
#                 draw_val(k, r, c)
#                 pg.display.flip()
#                 pg.time.delay(50)
#                 # Move to the next column within the same row
#                 return solve(grid, r, c + 1)
#             else:
#                 grid[r][c] = 0
#                 if c == 0:
#                     return solve(grid, r-1, c)
#                 else:
#                     return solve(grid , r ,c-1)
                
#         return False


#function to check if board is complete
def checkFinish(grid,i,j):
    while grid[i][j]!= 0:
        if i<8:
            i+= 1
        elif i == 8 and j<8:
            i = 0
            j+= 1
        elif i == 8 and j == 8:
            return True
    return False
    # pg.event.pump()
    # for it in range(1, 10):
    #     if valid(grid, i, j, it)== True:
    #             grid[i][j]= it
    #             global x, y
    #             x = i
    #             y = j
    #             # white color background
    #             screen.fill((255, 255, 255))
    #             draw()
    #             clickBox()
    #             pg.display.update()
    #             pg.time.delay(20)
    #             if solve(grid, i, j)== 1:
    #                 return True
    #             else:
    #                 grid[i][j]= 0
    #             # white color background\
    #             screen.fill((255, 255, 255))

    #             draw()
    #             clickBox()
    #             pg.display.update()
    #             pg.time.delay(50)
    # return False

                
def result():
    text_congratulations = font.render("CONGRATULATIONS YOU", 1, (0, 0, 255))

    # Render the second line
    text_won = font.render("WON", 1, (0, 0, 255))

    # Blit the first line onto the screen
    screen.blit(text_congratulations, (20, 500))

    # Calculate the position for the second line (under the first line)
    text_won_x = 300
    text_won_y = 500 + text_congratulations.get_height() + 5  # Adjust the vertical spacing as needed

    # Blit the second line onto the screen
    screen.blit(text_won, (text_won_x, text_won_y))
                
           
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
def draw_val(val,x,y):
    grid_x = int(x)
    grid_y = int(y)
    # print('these are the grid coords',grid_x,grid_y)
    #debugging
    # grid_x = int(x // diff)
    # grid_y = int(y // diff)
    # print('the number in this cell is ',number_grid[grid_y][grid_x])
    # print(grid_y,grid_x)
    if number_grid[grid_y][grid_x] == 0:
        # print('this square is empty')
        pg.draw.rect(screen, (255,255,255), ((x * diff+6)+15, (y * diff+6)+15, diff-13, diff-13))

        text1 = font2.render(str(val), 1, (0, 0, 255))
        screen.blit(text1, (x * diff+42, y * diff+37))

#function to check if the value works for the sudoky board,
#so that there is not the same number in the 3x3 square or in the row or column
def valid(grid, x, y, val):
    x = int(x)
    y = int(y)
    if grid[x][y] == val:
        return 'duplicate'
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

# def find_empty_cell(board):
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] == 0:
#                 return i, j
        
def solve(grid, row, col):
   
    
    if (row == 8 and col == 9):
        return True
       
    
    if col == 9:
        row += 1
        col = 0
 
    
    if grid[row][col] > 0:
        return solve(grid, row, col + 1)
    for num in range(1, 9 + 1, 1):
       
        
        if valid(grid, row, col, num):
           
            
            grid[row][col] = num
            draw_val(num, col, row)
            pg.display.flip()
            pg.time.delay(20)
 
            
            if solve(grid, row, col + 1):
                return True
 

        grid[row][col] = 0
        draw_val(num, col, row)
        pg.display.flip()
        pg.time.delay(20)
    return False




# mouse_clicked = False
res = 0
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
            clickBox(x,y)
            pg.display.flip()
            pg.time.delay(50)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x-= 1
                clickBox(x,y)
                
            if event.key == pg.K_RIGHT:
                x+= 1
                clickBox(x,y)
                
            if event.key == pg.K_UP:
                y-= 1
                clickBox(x,y)
                
            if event.key == pg.K_DOWN:
                y+= 1
                clickBox(x,y)
                
                
            if event.key == pg.K_1 or event.key == pg.K_KP1:
                val = 1
            if event.key == pg.K_2 or event.key == pg.K_KP2:
                val = 2
            if event.key == pg.K_3 or event.key == pg.K_KP3:
                val = 3
            if event.key == pg.K_4 or event.key == pg.K_KP4:
                val = 4
            if event.key == pg.K_5 or event.key == pg.K_KP5:
                val = 5
            if event.key == pg.K_6 or event.key == pg.K_KP6:
                val = 6
            if event.key == pg.K_7 or event.key == pg.K_KP7:
                val = 7
            if event.key == pg.K_8 or event.key == pg.K_KP8:
                val = 8
            if event.key == pg.K_9 or event.key == pg.K_KP9:
                val = 9
            if event.key == pg.K_BACKSPACE:
                # Reset number
                val = 0
                solve_number_grid[int(y)][int(x)] = 0
                # Clear input box
                pg.draw.rect(screen, (255,255,255), ((x * diff+6)+15, (y * diff+6)+15, diff-13, diff-13))
            if event.key == pg.K_SPACE:
                val = 0
                print('space clicked')

                solve(solve_number_grid,0,0)
                # draw_numbers()
                pg.display.flip()
                # print(solve_number_grid)
            
        
        if val != 0:
            # get_cord(pg.mouse.get_pos())
            
            if valid(solve_number_grid,y,x,val) == 'duplicate':
                print('dupe')
                validNum = True
            elif valid(solve_number_grid,y,x,val) == True:
                solve_number_grid[int(y)][int(x)] = val
                pg.draw.rect(screen, (0,0,255), ((x * diff+6)+15, (y * diff+6)+15, diff-13, diff-13))
                pg.display.flip()
                pg.time.delay(100)
                pg.draw.rect(screen, (255,255,255), ((x * diff+6)+15, (y * diff+6)+15, diff-13, diff-13))
                validNum = True
                print('it works')
            if validNum == False:
                pg.draw.rect(screen, (255,0,0), ((x * diff+3)+15, (y * diff+3)+15, diff-7, diff-7))
                pg.display.flip()
                pg.time.delay(100)
                pg.draw.rect(screen, (255,255,255), ((x * diff+3)+15, (y * diff+3)+15, diff-7, diff-7))
            elif validNum == True:
                draw_val(val,x,y)
                validNum = False
            
            # pg.display.flip()
            
            val = 0
            # pg.time.delay(50)
            # mouse_clicked = False
        if checkFinish(solve_number_grid,0,0) == True:
            res = 1
        if res == 1:
            result()

    

    
    draw_numbers()#this is the function to draw the numbers he
    pg.display.flip()





    
