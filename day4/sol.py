#!/usr/bin/env python3
def p1(arr, optarr):
    valid = 0
    for ids in arr:
        isvalid = True
        for req in optarr:
            if ids.get(req) is None:
                isvalid = False
                break
        if isvalid:
            valid = valid + 1
    return valid

def p1(arr, optarr):
    valid = 0
    for ids in arr:
        isvalid = True
        for req in optarr:
            if ids.get(req) is None:
                isvalid = False
                break
            if int(ids.get(byr)) < 1920 or int(ids.get(byr)) > 2020:
                isvalid = False
                break
            if int(ids.get(iyr)) < 1920 or int(ids.get(iyr)) > 2020:
                isvalid = False
                break
            if int(ids.get(eyr)) < 1920 or int(ids.get(eyr)) > 2020:
                isvalid = False
                break
        if isvalid:
            valid = valid + 1
    return valid

def main():
    arr = []
    with open("./input.txt") as inp:
        ids = dict()
        for line in inp:
            line = line.strip()
            if len(line) == 0:
                arr.append(ids)
                ids = dict()
            line = line.split()
            for item in line:
                item = item.split(":")
                ids[item[0]] = item[1]

    print(p1(arr, ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]))

if __name__ == "__main__":
    main()
