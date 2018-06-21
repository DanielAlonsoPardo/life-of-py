



class GameOfLife:
    #Board tracks every relevant cell, AKA all live cells + every dead cell with live neighbors
    board = {}

    #Make dictionary of cells
    #{'x,y':Bool}
    #At every iteration:
    #Check each live and dead cell in the dic
    #If the cell lives, add its neighbors to the dic
    #if it dies, and it has no neighbors, remove from dic


    #Count the number of neighboring cells that are alive
    #next to the given cell
    def neighbor_count(self, cell):
        pass

    #Set the life status of a cell to alive
    ##Also adds neighboring cells to the board
    def revive(self, cell):
        
        pass

    #Set the life status of a cell to dead
    ##Also removes the cell from the board if it has no live neighbors
    def kill(self, cell):
        pass

    #
    def exists(self, cell):
        pass

    #go forwards one turn
    def step(self):
        for cell, alive in self.board[:].items():
            count = self.neighbor_count(cell)
            if alive and ((count > 3) or (count < 2)):
                self.kill(cell)
            elif not alive and (count == 3):
                self.revive(cell)

