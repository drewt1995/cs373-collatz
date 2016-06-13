#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read(line):
    """
    read two ints
    s a string
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
    max_length = 0


    for value in range(i, j+1):
        count = 1
        while value != 1:
            if value % 2 == 0:
                value /= 2
            else:
                value = (value * 3) + 1
            count += 1
        if count > max_length:
            max_length = count

    return max_length

# -------------
# collatz_print
# -------------


def collatz_print(writer, start, end, max_length):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    writer.write(str(start) + " " + str(end) + " " + str(max_length) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(reader, writer):
    """
    r a reader
    w a writer
    """
    for line in reader:
        start, end = collatz_read(line)
        max_length = collatz_eval(start, end)
        collatz_print(writer, start, end, max_length)
