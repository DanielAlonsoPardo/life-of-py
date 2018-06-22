from life import GameOfLife
import time


foo = GameOfLife()

foo.revive("0,0")
foo.revive("1,0")
foo.revive("2,0")
foo.revive("-1,1")
foo.revive("-3,0")
foo.revive("-4,0")
foo.revive("-3,2")


foo.render()

for cell, alive in foo.board.items():
    print(cell, alive)


def loop():
    while True: foo.step(); foo.render(); time.sleep(0.1)
