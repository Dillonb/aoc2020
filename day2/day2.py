#!/usr/bin/env python3

def is_valid_policyone(letter, min_, max_, password):
    count = password.count(letter)
    return (count >= min_) and (count <= max_)


def at(s, x):
    return s[x - 1]


def is_valid_policytwo(letter, posa, posb, password):
    return (at(password, posa) == letter) != (at(password, posb) == letter)


num_valid_policyone = 0
num_valid_policytwo = 0

for line in open("input"):
    policy, password = line.split(":")
    ab, letter = policy.split(" ")
    a, b = ab.split("-")
    a = int(a)
    b = int(b)
    password = password.strip()

    num_valid_policyone += (1 if is_valid_policyone(letter, a, b, password) else 0)
    num_valid_policytwo += (1 if is_valid_policytwo(letter, a, b, password) else 0)

print("Num valid policy one: %d" % num_valid_policyone)
print("Num valid policy two: %d" % num_valid_policytwo)
