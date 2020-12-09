#!/usr/bin/env python3

import re
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

def p2(arr, optarr):
    valid = 0
    eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for ids in arr:
        isvalid = True
        for req in optarr:
            if ids.get(req) is None:
                isvalid = False
                break
        if not isvalid:
            continue
        if int(ids.get("byr")) < 1920 or int(ids.get("byr")) > 2002:
            isvalid = False
            continue
        if int(ids.get("iyr")) < 2010 or int(ids.get("iyr")) > 2020:
            isvalid = False
            continue
        if int(ids.get("eyr")) < 2020 or int(ids.get("eyr")) > 2030:
            isvalid = False
            continue
        mins = 150
        most = 193
        if ids.get("hgt").find("in") != -1:
            mins = 59
            most = 76
        elif ids.get("hgt").find("cm") == -1:
            isvalid = False
            continue
        height = ids.get("hgt")[:-2]
        height = int(height)
        if height < mins or height > most:
            isvalid = False
            continue

        if ids.get("ecl") not in eyes:
            isvalid = False
            continue

        hcl = ids.get("hcl")
        if re.search('^#[0-9a-f]{6}$', hcl) is None:
            isvalid = False
            continue

        pid = ids.get("pid")
        if re.search('^[0-9]{9}$', pid) is None:
            isvalid = False
            continue

        print(ids, isvalid)


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
    print(p2(arr, ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]))

if __name__ == "__main__":
    main()
