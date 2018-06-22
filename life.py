def neighbours(cell):
    position = cell.split(",")
    for x in range(-1, 2):
        for y in range(-1, 2):
            if not (x == y == 0):
                yield "%i,%i" % (position[0] + x, position[1] + y)

class GameOfLife:
    #Board tracks every relevant cell, AKA all live cells + every dead cell with live neighbors
    board = none

    def __init__(self):
        self.board = {}
    

    #Make dictionary of cells
    #{'x,y':Bool}
    #At every iteration:
    #Check each live and dead cell in the dic
    #If the cell lives, add its neighbors to the dic
    #if it dies, and it has no neighbors, remove from dic


    #Count the number of neighboring cells that are alive
    #next to the given cell
    def neighbor_count(self, cell):
        count = 0
        for neighbour in neighbours(cell):
            if self.is_alive(neighbour):
                count += 1
        return count

    #Very self descriptive
    def is_alive(self, cell):
        if cell in self.board:
            return self.board[cell]
        return False

    #Set the life status of a cell to alive
    ##Also adds neighboring cells to the board
    def revive(self, cell):
        self.board[cell] = True
        for neighbour in neighbours(cell):
            if cell not in self.board:
                self.board[cell] = False

    #Set the life status of a cell to dead
    ##Also removes the cell from the board if it has no live neighbors
    def kill(self, cell):
        if self.neighbour_count(cell) == 0:
            del self.board[cell]
        else:
            self.board[cell] = False

    #go forwards one turn
    def step(self):
        for cell, alive in self.board[:].items():
            count = self.neighbor_count(cell)
            if alive and ((count > 3) or (count < 2)):
                self.kill(cell)
            elif not alive and (count == 3):
                self.revive(cell)

    #Print to terminal
    #80 x 23
    #-40 <===> 39
    #-11 <===> 11
    def render(self):
        for y in range(11, -12, -1):
            line = "                                                                                "
            for x in range(-40, 40):
                if self.is_alive("%i,%i" % (x, y)):
                    line[x] = "x"
            print(line)
