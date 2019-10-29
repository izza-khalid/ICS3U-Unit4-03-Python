#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: Oct 2019
# This program uses a for loop


def main():
    # this function uses a for loop
    counter = 0
    answer = 0

    # input
    print("We will find squares of whole numbers!!")
    number = int(input("Enter a positive integer: "))
    print("")

    # process & output
    for counter in range(number + 1):
        answer = counter**2
        print("{0}² = {1} ".format(counter, answer))


if __name__ == "__main__":
    main()
