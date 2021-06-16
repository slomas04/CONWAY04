###### Conway's Game of Life ######
###### made by Samuel Lomas
###### github: https://github.com/slomas04
import time as t
import random as r

###### GET SCREEN SIZE ######

usrheight = input("Enter the Grid height:\t\t(leave blank for 26)\n\t>>> ")
usrwidth = input("Enter the Grid width:\t\t(leave blank for 75)\n\t>>> ")

if usrheight == "":
    gridheight = 26
else:
    try:
        gridheight = int(usrheight)
    except:
        print("Not a Number! Defaulting to 26.")
        gridheight = 26
        
if usrwidth == "":
    gridwidth = 75
else:
    try:
        gridwidth = int(usrwidth)
    except:
        print("Not a Number! Defaulting to 75.")
        gridwidth = 75
        
###### PRINT FUNCTION ######

def printgrid(grid): #Super Snazzy optimised print function I made, it compiles the entire array and details down to one string, therefore speeding up the framerate
    outstring = ""
    outstring += ("█"*(gridwidth + 2))
    outstring += ("\n")
    for i in range(gridheight):
        outstring += "█"
        for j in range(gridwidth):
            outstring += grid[j][i]
        outstring += "█"
        outstring += "\n"
    outstring += ("█"*(gridwidth + 2))
    outstring += "\n"
    return outstring

###### GRID EDITOR ######

def editgrid(grid):
    while True:
        print(printgrid(grid))
        coords = input("Enter the coords you wish to place/flip\t\t'exit' to leave the editor\nSeparate coordinates with space\n\t>>> ")

        if coords == "exit":
            break
        else:
            try:
                coords = coords.split(' ')
                xcord = int(coords[0]) - 1
                ycord = gridheight - int(coords[1])

                if grid[xcord][ycord] == "▓":
                    grid[xcord][ycord] = " "

                elif grid[xcord][ycord] == " ":
                    grid[xcord][ycord] = "▓"
                        
            except:
                print("Coordinates not Valid!")
                
        

    return grid

###### COUNT LIVING NEIGHBORS ######

def numneighbors(grid, row, col): #long and probably innefficient function that returns the number of living neighbors a cell has
    num = 0
    try:
        if grid[row + 1][col] == "▓":
            num += 1
    except:
        pass
    try:
        if grid[row - 1][col] == "▓":
            num += 1
    except:
        pass
    try:
        if grid[row][col + 1] == "▓":
            num += 1
    except:
        pass
    try:
        if grid[row][col - 1] == "▓":
            num += 1
    except:
        pass
    try:
        if grid[row + 1][col + 1] == "▓":
            num += 1
    except:
        pass
    try:
        if grid[row + 1][col - 1] == "▓":
            num += 1
    except:
        pass
    try:
        if grid[row - 1][col + 1] == "▓":
            num += 1
    except:
        pass
    try:
        if grid[row - 1][col - 1] == "▓":
            num += 1
    except:
        pass
    
    return num
    
    
###### GENERATE PIXEL GRID ######

pixelgrid = [[" " for y in range (gridheight)] for x in range(gridwidth)]

for i in range(gridheight):
    for j in range(gridwidth):
        if r.randint(0,1) == 1: 
            pixelgrid[j][i] = "▓"
        else:
            pixelgrid[j][i] = " "

print(printgrid(pixelgrid))

if input("This is a randomised grid. Type 1 and hit enter to wipe the grid and manually customise it.\nIf not, Hit enter to continue.\n\t>>> ") == "1": # Give user the choice to manually edit grid
    pixelgrid = [[" " for y in range (gridheight)] for x in range(gridwidth)]
    pixelgrid = editgrid(pixelgrid)
    print(printgrid(pixelgrid))
    input("Press Enter to Start... ")
else:
    pass

###### MAINLOOP ######

while True:
    newiteration = [[" " for y in range (gridheight)] for x in range(gridwidth)] #create a new grid to iterate onto
    for j in range(gridheight):
        
        for i in range(gridwidth):
            
            livingneighbors = numneighbors(pixelgrid, i, j)
            
            if pixelgrid[i][j] == " ":
                if livingneighbors == 3:
                    newiteration[i][j] = "▓" #If a dead cell has three living neighbors, it comes to life
                    
            elif pixelgrid[i][j] == "▓":
                if (livingneighbors == 2) or (livingneighbors == 3):
                    newiteration[i][j] = "▓" #If a living cell has two or three neighbors, it continues.
                
                elif (livingneighbors < 2) or (livingneighbors > 3):
                    newiteration[i][j] = " " #If a living cell has one or less than two or more than three neighbors, it dies
    
    
    pixelgrid = newiteration #save the new grid iteration
    print(printgrid(pixelgrid)) #print
    t.sleep(0.01)

