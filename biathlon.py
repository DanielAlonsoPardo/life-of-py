#!/usr/bin/python3
import sys
import time
import importlib.util
from subprocess import PIPE, run

#[!]switch to timeit 

"""
biathlon.py

This program makes Life run a biathlon: golf + marathon.
It must therefore test:

1.- Correctness of the Life implementation
2.- Time taken to reach a given generation (marathon)
3.- Code length not counting comments (golf)

To test points 1 & 2, the "Acorn" pattern should be loaded and run for 5206 generations, which is the time it takes for its population to reach a plateau.
"""


#Get name of file implementing Conway's Game of Life
if (len(sys.argv) < 2):
    print("Usage:")
    print(sys.argv[0] + " <filename>")
    print("")
    print("This script tests the length of a Game of Life implementation and its efficiency.")
    print("It counts the length of the code, and it records the length of time it takes to run the Acorn pattern for 5206 generations.")
    sys.exit()

#Load it
life_filename = sys.argv[1]
spec = importlib.util.spec_from_file_location("life", life_filename)
life = importlib.util.module_from_spec(spec)
spec.loader.exec_module(life)

#Seed it
acorn = ("0,0", "1,0", "2,0", "-1,1", "-3,0", "-4,0", "-3,2")
world = life.GameOfLife(seed=acorn)

#Run and time it until Acorn reaches plateau

start = time.clock()
for iteration in range(5206):
    world.step()
end = time.clock()

#Check board state

print("correctness not implemented")

#Count non-comment, non-empty lines (assume no multiline shenanigans for both code and comments)
args = ('egrep -vc (^\s*#)|(^\s*$) ' + life_filename).split()

line_count = int(run(args, stdout=PIPE).stdout)

#Print results to stdout
print("Length of code:", line_count, "lines")
print("Execution time:", end - start)

world.render()

def loop():
    while True: universe.step(); universe.render(); time.sleep(0.1)
