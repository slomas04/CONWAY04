### Conway's Game of Life
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
    
###### GENERATE PIXEL GRID ######

pixelgrid = [[" " for y in range (gridheight)] for x in range(gridwidth)]

print(printgrid(pixelgrid))

input("Press enter...")

####### RANDOM FILL ######

while True:
    for i in range(gridheight):
        for j in range(gridwidth):
            if r.randint(0,1) == 1: 
                pixelgrid[j][i] = "▓"
            else:
                pixelgrid[j][i] = " "

    
    print(printgrid(pixelgrid))
    t.sleep(0.01)

##for j in range(gridheight):
##    for i in range(gridwidth+2):
##        try:
##            pixelgrid[i][j] = "▓"
##        except:
##            pass
##        try:
##            pixelgrid[i-2][j] = " "
##        except:
##            pass
##        print(printgrid(pixelgrid))
##        t.sleep(0.01)
##        #input("Press enter...")

