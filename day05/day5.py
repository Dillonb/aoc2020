#!/usr/bin/env python3

def spacepart(s, l, u, min_, max_):
    for c in s:
        range_ = max_ - min_
        if c == l:
            max_ = min_ + int(range_ / 2)
            pass
        elif c == u:
            min_ = max_ - int(range_ / 2)
    return min_

def get_seat_id(s):
    row = spacepart(s[:7], "F", "B", 0, 127)
    seat = spacepart(s[7:], "L", "R", 0, 7)
    return row * 8 + seat

seat_ids = []
for seat in open("input"):
    seat_ids.append(get_seat_id(seat.strip()))

print("Highest seat id: %d" % max(seat_ids))

seat_ids = sorted(seat_ids)

for i in range(0, len(seat_ids) - 1):
    if seat_ids[i + 1] - seat_ids[i] != 1:
        print("Your seat id: %d" % (seat_ids[i] + 1))
