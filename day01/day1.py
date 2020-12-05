#!/usr/bin/env python3

f = open("input")

ints = []

for l in f:
    ints.append(int(l.strip()))

for i in ints:
    for j in ints:
        if (i + j) == 2020:
            print("%d * %d = %d" % (i, j, i * j))

for i in ints:
    for j in ints:
        for k in ints:
            if (i + j + k) == 2020:
                print("%d * %d * %d = %d" % (i, j, k, i * j * k))
