#!/usr/bin/env python3
import re

passports = []

current_passport = {}

for line in open("input"):
    line = line.strip()

    if len(line) == 0:
        passports.append(current_passport)
        current_passport = {}
    else:
        for field in line.split(" "):
            name, value = field.split(":")
            current_passport[name] = value

passports.append(current_passport)

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def validate_hgt(hgt):
    incm = hgt[-2:]
    if incm == "cm":
        val = int(hgt[:-2])
        return val >= 150 and val <= 193
    elif incm == "in":
        val = int(hgt[:-2])
        return val >= 59 and val <= 76
    else:
        return False

valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

is_4dgt = lambda x: re.match("\d\d\d\d", x)

validators = {
    "byr": lambda x: is_4dgt(x) and int(x) >= 1920 and int(x) <= 2002,
    "iyr": lambda x: is_4dgt(x) and int(x) >= 2010 and int(x) <= 2020,
    "eyr": lambda x: is_4dgt(x) and int(x) >= 2020 and int(x) <= 2030,
    "hgt": validate_hgt,
    "hcl": lambda x: re.match("^#[0-9a-f]{6}$", x),
    "ecl": lambda x: x in valid_ecl,
    "pid": lambda x: re.match("^\d{9}$", x)
}

def is_valid_partone(passport):
    for reqfield in required_fields:
        if reqfield not in passport.keys():
            return False
    return True

def is_valid_parttwo(passport):
    for reqfield in required_fields:
        if reqfield not in passport.keys():
            return False
        else:
            if not validators[reqfield](passport[reqfield]):
                return False

    return True


num_valid_partone = 0
num_valid_parttwo = 0

for passport in passports:
    if is_valid_partone(passport):
        num_valid_partone += 1

    if is_valid_parttwo(passport):
        num_valid_parttwo += 1

print ("num valid part one: %d" % num_valid_partone)
print ("num valid part two: %d" % num_valid_parttwo)
