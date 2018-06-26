def neighbours(cell):
    position = cell.split(",")
    for x in range(-1, 2):
        for y in range(-1, 2):
            if not (x == y == 0):
                yield "%i,%i" % (int(position[0]) + x, int(position[1]) + y)

class GameOfLife:
    #Board tracks every relevant cell, AKA all live cells + every dead cell with live neighbours
    board = {}

    def __init__(self, seed=()):
        self.board = {}
        for cell in seed:
            self.revive(cell)
    

    #Make dictionary of cells
    #{'x,y':Bool}
    #At every iteration:
    #Check each live and dead cell in the dic
    #If the cell lives, add its neighbours to the dic
    #if it dies, and it has no neighbours, remove from dic


    #Count the number of neighbouring cells that are alive
    #next to the given cell
    def neighbour_count(self, cell):
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
    ##Also adds neighbouring cells to the board
    def revive(self, cell):
        self.board[cell] = True
        for neighbour in neighbours(cell):
            if neighbour not in self.board:
                self.board[neighbour] = False

    #Set the life status of a cell to dead
    ##Also removes the cell from the board if it has no live neighbours
    def kill(self, cell):
        if self.neighbour_count(cell) == 0:
            del self.board[cell]
        else:
            self.board[cell] = False

    #go forwards one turn
    def step(self):
        next_step = GameOfLife()
        next_step.board = self.board.copy()

        for cell, alive in self.board.items():
            count = self.neighbour_count(cell)
            if alive and ((count > 3) or (count < 2)):
                next_step.kill(cell)
            elif not alive and (count == 3):
                next_step.revive(cell)
        self.board = next_step.board

    #Print to terminal
    #80 x 23
    #-40 <===> 39
    #-11 <===> 11
    def render(self):
        for y in range(11, -12, -1):
            line = ""
            for x in range(-40, 40):
                if self.is_alive("%i,%i" % (x, y)):
                    line += "x"
                else:
                    line += " "
            print(line)
