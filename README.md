# Sudoku
pygame Sudoku

main.py
this project is made with pygame, and is a simple sudoku game that also incorporates a Sudoku solver that uses backtracking and recursion
these are all the functions i have used and also their functionality to complete the mini project
i first declared the grid and the basic things like the screen size
and also made a duplicate of the grid so that i can use it behind the scenes

def draw()
this function draws the 10 lines vertically and 10 lines horizontally to create the Sudoky board

def get_cord(pos)
this function gets the co-ordinates of the mouse and i call this function when i click the mouse (pg.mouse.get_pos()) and assigns the x and y coordinates as global variables meaning i can use them throughout the code

def clickBox(x,y)
this function is for the sole purpose of knowing which box to highlight, it uses the x coordinates and y coordinates of the mouse click to find out which box to highlight and then it calls the highlight function
i also made it so the arrow keys work, so left moves the highlighted box left etc

def highlight_box(x,y,mouse_click)
this function checks if the mouse_click if true or not depending on the clickBox function and then depending that draws a red box around the chosen box, when another box is clicked the draw() function is called meaning that the red box gets drawn over (disappears) showing the new red box in a different location

def checkFinish(grid,i,j)
this is a simple function that checks if the grid is filled out, checking if i (the x value) and j (the y value) have reached the max (index value 8) checking each box in the process to see if the boxes are NOT 0
grid[i][j] != 0

def result()
simple function that if checkFinish() then return a text on the screen saying congratulations you won meaning you have completed the game

def draw_numbers()
this is the function to draw the hard coded numbers of the original grid, it alocated the specified number of e.g. index 0,0 of the grid to index 0,0 of the visual grid on the screen and renders it to the screen

def draw_val(val,x,y)
this function draw the val you have entered through the keyboard and using the clickBox() function to decide which box to enter the number into, but it takes the value you have inputted and outputs the value into the selected box

def valid(grid,x,y,val)
this checks if the value entered into the box is valid, it checks if the number is in the row selected and then checks if the number is in the column selected, and also finally checks if it appears in the same 3x3 box just like sudoku, if it appears in the box it returns false meaning the number is not valid and it does not let you input the number, but if it returns true it means it is valid and the number is not blocked by another number in the same box, row or column. i also have return 'duplicate' when the box already has the number you are trying to input

def solve(grid, row, col)
this is the main function that solves the sudoku no matter the puzzle or sequence, it uses backtracking and recursion. backtracking means that it selects valid numbers and proceeds through the rows and columns until a box has no valid entries, it then backtracks and changes the previous box to another valid number to check to see if the box after it has valid entries. It does this throughout the whole sudoku grid until it finds a viable solution, if it returns false that means that there is no solution. Recursion is a function using itself inside the function. I used recursion in this instance to create an efficient way to go through the rows and columns. this function eventually solves the sudoku puzzle and uses the draw_val() and pg.display.flip() and pg.time.delay(50) to show the process as it is happening.

And then my main loop that keeps the game running checks for the key clicks based on the key click i run the desired function. i also check when the value is not 0 ( if val != 0 ) then if the value is valid or a duplicate and if it is valid then draw_val(). and then finally i check if the board is finished checkFinish() and if its true return the text result(). and then at the bottom of the loop is pg.display.flip() which updates the board. to exit i just press x on the tab. And putting all of those together i have a working sudoku game and a working sudoku solver when i hit the space bar at any point during my solve.






