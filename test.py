from life import GameOfLife


foo = GameOfLife()

foo.revive("-1,0")
foo.revive("0,0")
foo.revive("1,0")

foo.render()

for cell, alive in foo.board.items():
    print(cell, alive)
