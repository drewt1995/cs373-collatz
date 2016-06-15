#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

CACHE = {}

# ------------
# collatz_read
# ------------
MINVAL = 0
TESTVAL = 837799
MAXVAL = 1000000
MAXCYCLE = 525


def collatz_read(line):
    """
    read two ints
    line a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    tokens = line.split()
    return [int(tokens[0]), int(tokens[1])]

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i > 0
    assert j < 1000000
    global CACHE

    if i <= TESTVAL <= j:
        return MAXCYCLE

    if not CACHE:
        CACHE = {1:1}
        for val in range(2, MAXVAL + 1):
            temp = val
            count = 1
            while val != 1:
                if val in CACHE:
                    count += CACHE.get(val) - 1
                    break
                if val % 2 == 0:
                    val >>= 1
                    count += 1
                else:
                    val = val + (val >> 1) + 1
                    count += 2
            CACHE.update({temp:count})


    if i > j:
        temp = j
        j = i
        i = temp

    if (j // 2) + 1 > i:
        values = range((j // 2) + 1, j+1)
    else:
        values = range(i, j+1)


    max_value = 1
    for value in values:
        tmp = CACHE.get(value)
        if tmp > max_value:
            max_value = tmp

    assert max_value != 0
    return max_value

# -------------
# collatz_print
# -------------


def collatz_print(writer, start, end, max_length):
    """
    print three ints
    writer a writer
    start the beginning of the range, inclusive
    end the end       of the range, inclusive
    max_length the max cycle length
    """
    writer.write(str(start) + " " + str(end) + " " + str(max_length) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    for line in reader:
        start, end = collatz_read(line)
        max_length = collatz_eval(start, end)
        collatz_print(writer, start, end, max_length)
