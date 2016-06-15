#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        line = "1 10\n"
        i, j = collatz_read(line)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        line = "499 500\n"
        i, j = collatz_read(line)
        self.assertEqual(i,  499)
        self.assertEqual(j, 500)

    def test_read_3(self):
        line = "1 1000\n"
        i, j = collatz_read(line)
        self.assertEqual(i,  1)
        self.assertEqual(j, 1000)

    # ----
    # eval
    # ----
    def test_eval_1(self):
        val = collatz_eval(1, 999999)
        self.assertEqual(val, 525)

    def test_eval_2(self):
        val = collatz_eval(1, 10)
        self.assertEqual(val, 20)

    def test_eval_3(self):
        val = collatz_eval(100, 200)
        self.assertEqual(val, 125)

    def test_eval_4(self):
        val = collatz_eval(201, 210)
        self.assertEqual(val, 89)

    def test_eval_5(self):
        val = collatz_eval(900, 1000)
        self.assertEqual(val, 174)

    def test_eval_6(self):
        value = collatz_eval(1, 1)
        self.assertEqual(value, 1)

    def test_eval_7(self):
        val = collatz_eval(200, 100)
        self.assertEqual(val, 125)

    def test_eval_8(self):
        val = collatz_eval(200000, 201)
        self.assertEqual(val, 383)

    def test_eval_9(self):
        val = collatz_eval(10, 1)
        self.assertEqual(val, 20)

    # -----
    # print
    # -----

    def test_print_1(self):
        write = StringIO()
        collatz_print(write, 1, 10, 20)
        self.assertEqual(write.getvalue(), "1 10 20\n")

    def test_print_2(self):
        write = StringIO()
        collatz_print(write, 1, 999999, 5477898)
        self.assertEqual(write.getvalue(), "1 999999 5477898\n")

    def test_print_3(self):
        write = StringIO()
        collatz_print(write, 1, 10, 20)
        self.assertEqual(write.getvalue(), "1 10 20\n")
    # -----
    # solve
    # -----

    def test_solve_1(self):
        read = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        read = StringIO("1 2000\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), "1 2000 182\n")

    def test_solve_3(self):
        read = StringIO("10 10\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), "10 10 7\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
