#!/usr/bin/env python3
def main():
    arr = []
    with open("./input.txt") as inp:
        for line in inp:
            arr.append(int(line.strip()))
    for i in arr:
        for j in arr:
            if i + j == 2020:
                print(i * j)
            for k in arr:
                if i + j + k == 2020:
                    print(i * j * k)
                    return
if __name__ == "__main__":
    main()
