""" Conway game of life """
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells: 
nextCells = []
for x in range(WIDTH):
    column = [] # Create new column
    for y in range(HEIGHT):
        if (random.randint(0,1) == 0): #Returns an integer equal or higher than 0 and lower or equal to 1
            column.append('#') # Add a living cell if random int is 0
        else:
            column.append(' ')
    nextCells.append(column) # Nextcells is a list of columns

# Main program loop:
while True:
    print('\n\n\n\n\n') # Print 5 new lines
    currentCells = copy.deepcopy(nextCells) # Create new reference to cells

    # Print current cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') #Print the # or space
        print()

    # Calculate the next step's cell based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates 
            # '% WIDTH' ensures leftCoor is always between 0 and width -1 

            leftCoord = (x - 1) % WIDTH # If -1, evaluates to 59
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbords:
            numNeighbors = 0
            if (currentCells[leftCoord][aboveCoord] == '#'):
                numNeighbors += 1 # Top left neighbor is alive
            if (currentCells[x][aboveCoord] == '#'):
                numNeighbors += 1 # Top neighbor is alive
            if (currentCells[rightCoord][aboveCoord] == '#'):
                numNeighbors += 1 # Top right neighbor is alive
            if (currentCells[leftCoord][y] == '#'):
                numNeighbors += 1 # Left neighbor is alive
            if (currentCells[rightCoord][y] == '#'):
                numNeighbors += 1 # Right neighbor is alive
            if (currentCells[leftCoord][belowCoord] == '#'):
                numNeighbors += 1 # Below left neighbor is alive
            if (currentCells[x][belowCoord] == '#'):
                numNeighbors += 1 # Below neighbor is alive
            if (currentCells[rightCoord][belowCoord] == '#'):
                numNeighbors += 1 # Below right neighbor is alive
            
            if (currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3)):
                nextCells[x][y] = '#' # Living cells with 2 or 3 neighbors stay alive
            elif (currentCells[x][y] == ' ' and numNeighbors == 3):
                nextCells[x][y] = '#' # Dead cells with 3 neighbors become alive
            else:
                nextCells[x][y] = ' ' # All others become or stay dead
        
    time.sleep(1) # Set a 1 second pause to reduce flickering
