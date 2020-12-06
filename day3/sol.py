#!/usr/bin/env python3
def p1(arr, right, down):
    tree = 0
    x = 0
    y = 0
    while True:
        if arr[x][y] == "#":
            tree = tree + 1
        x = x + down
        y = y + right
        if x >= len(arr):
            break
        if y >= len(arr[x]):
            y = y - len(arr[x])

    return(tree)

    print(valid)

def main():
    arr = []
    with open("./input.txt") as inp:
        for line in inp:
            line = line.strip()
            arr.append(line)
    print(p1(arr, 3, 1))
    print(p1(arr, 1, 1) * p1(arr, 3, 1) * p1(arr, 5, 1) * p1(arr,7,1) * p1(arr, 1, 2))
    #p1(arr)
    #p2(arr)

if __name__ == "__main__":
    main()
