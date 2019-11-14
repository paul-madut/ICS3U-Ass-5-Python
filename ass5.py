#!/usr/bin/env python3

# Created by: Paul M
# Created on: Oct 2019
# This program uses a while loop


def main():
    # this function uses a while loop
    # input
    word = input("What word would you like looped: \n")
    wordchar = input("How many characters would you like looped: \n")
    wordloop = input("How many times would you like this word looped: \n")
    # try statement
    try:
        wordchar_int = int(wordchar)
        wordloop_int = int(wordloop)
        if word.isnumeric():
            print("You did not input a valid word")
            return
        # process and output
        wordprint = word[0:wordchar_int]
        while (wordloop_int > 0):
            print(wordprint, end='')
            wordloop_int = wordloop_int - 1

    except Exception:
        print("That is not a valid response")


if __name__ == "__main__":
    main()
