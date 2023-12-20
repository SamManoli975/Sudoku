import pygame as pg
import sys

pg.init()
size = (750, 750)  # Width, Height
screen = pg.display.set_mode(size)
font = pg.font.SysFont('none', 80)
pg.display.set_caption("My Pygame Window")

x=0
y=0
diff = 750 / 9

number_grid = [
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

    
]



def get_cord(pos):
       global x
       x = pos[0]//diff
       global y
       y = pos[1]//diff

def clickBox():  
    print('yeah')
    # click = pg.mouse.get_pressed()
    if pg.mouse.get_pressed()[0]:  # Check if the left mouse button is pressed
        print('clicked')
        # screen.fill((0,0,0))
        pg.draw.line(screen, (255, 0, 0), (500, 500), (100, 0), 20)
        
            

            
        print(pg.mouse.get_pos())
        # if pos[0] in range(0,80) and pos[1] in range(0,80):
            
        #     pg.draw.line(screen, (255, 0, 0), (50 * diff-3, (50 + 1)*diff), (50 * diff + diff + 3, (50 + 1)*diff), 7)
        #     pg.draw.line(screen, (255, 0, 0), ( (50 + 1)* diff, 50* diff ), ((50 + 1) * diff, 50 * diff + diff), 7)
        # elif pos[0] in range(80,160) and pos[1] in range(0,80):
        #     print("Box 2 clicked")



def draw():
    screen.fill((0,0,0))
    for i in range(0,10):#looping through from 0-9
        line_width = 10 if i%3 == 0 else 3#changing line width to clearly show the 9 squares 
        #drawing lines
        pg.draw.line(screen,(255,255,255), ((80*i)+15,15),((80*i)+15,735),line_width)
        pg.draw.line(screen,(255,255,255), (15,(80*i)+15),(735,(80*i)+15),line_width)

        # pg.draw.lines(screen, (255,255,255), False, (80,0),(80,720), 3)
        
def draw_numbers():
    row = 0
    offset = 35
    while row < 9:
    
        col = 0
        while col < 9:
            number = number_grid[row][col]
            # text_rect = text.get_rect()
            text = font.render(str(number), True, (255,255,255))
            # text_rect.center = ((col*80)+40, (row*80)+40)
            screen.blit(text, ((col*80) + offset+5, (row*80) + offset-2))
            
            col +=1
        row +=1



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
            clickBox()

            

    get_cord(pg.mouse.get_pos())

    draw()
    draw_numbers()
    # clickBox(pg.mouse.get_pos())
    pg.display.flip()





    
