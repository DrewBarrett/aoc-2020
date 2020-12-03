#!/usr/bin/env python3
def p1(arr):
    valid = 0
    for index in arr:
        count = 0
        for char in index["password"]:
            if char == index["letter"]:
                count = count + 1
        if count >= index["minn"] and count <= index["maxx"]:
            valid = valid + 1


    print(valid)
def p2(arr):
    valid = 0
    for index in arr:
        a = False
        b = False
        if index["password"][index["minn"]-1] == index["letter"]:
            a = True
        if index["password"][index["maxx"]-1] == index["letter"]:
            b = True
        if a or b:
            if not a or not b:
                valid = valid + 1


    print(valid)

def main():
    arr = []
    with open("./input.txt") as inp:
        for line in inp:
            pas = {
                "minn": "",
                "maxx": "",
                "letter": "",
                "password": ""
            }
            line = line.strip()
            first = line.split("-")
            pas["minn"] = int(first[0])
            pas["maxx"] = int(first[1].split(" ")[0])
            pas["letter"] = line.split(" ")[1][0]
            pas["password"] = line.split(" ")[-1]
            arr.append(pas)
    p1(arr)
    p2(arr)

if __name__ == "__main__":
    main()
