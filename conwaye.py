### Conway's Game of Life
import time as t
import random as r

gridheight = 30
gridwidth = 60

def printgrid(grid):
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
    

pixelgrid = [[" " for y in range (gridheight)] for x in range(gridwidth)]

print(printgrid(pixelgrid))

pixelgrid[2][4] = "▓"

input("Press enter...")

print(printgrid(pixelgrid))

input("Press enter...")

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

