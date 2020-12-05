#!/usr/bin/env python3
from functools import reduce

# load data

grid = []

for line in open("input"):
    row = []
    for char in line.strip():
        row.append(char)
    grid.append(row)

# part 1
def count_trees(xslope, yslope):
        trees_encountered = 0
        x = 0
        y = 0

        while y < len(grid):
            if grid[y][x % len(grid[y])] == "#":
                trees_encountered += 1
            y += yslope
            x += xslope
        return trees_encountered

print("Part 1:")
print("Encountered %d trees" % count_trees(3, 1))


# part 2
print("\nPart 2:")
print("Answer: %d" % reduce(lambda x, y: x * y, map(lambda slope: count_trees(slope[0], slope[1]), ((1,1), (3,1), (5,1), (7,1), (1,2))), 1))
