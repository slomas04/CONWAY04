### Conway's Game of Life

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
    return outstring
    

pixelgrid = [[" " for y in range (gridheight)] for x in range(gridwidth)]

print(printgrid(pixelgrid))

pixelgrid[2][4] = "▓"

input("Press enter...")

print(printgrid(pixelgrid))

input("Press enter...")

for i in range(gridwidth):
    pixelgrid[i][15] = "▓"
    try:
        pixelgrid[i-2][15] = " "
    except:
        pass
    print(printgrid(pixelgrid) + "\n")
    #input("Press enter...")

