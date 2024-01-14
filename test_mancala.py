# ********
# This file is individualized for NetID huxing.
# ********

import traceback
import sys
from mancala_helpers import *

def indent(s, prefix):
    return s.replace("\n", "\n" + prefix)

def format(value):
    if type(value) == str: return "'%s'" % value
    if type(value) == type(format): return value.__name__
    return str(value)

def run_test(function, arguments, target):
    arg_string = ", ".join(map(format, arguments))
    try:
        output = function(*arguments)
        if output == target: return 2
        else:
            print("  %s(%s) incorrect [-1pt]:" % (format(function), arg_string))
            print("  returned %s" % indent(format(output), "  "))
            print("  should return %s" % indent(format(target), "  "))
            return 1
    except Exception as error:
        print()
        print("  %s(%s) crashed with this error [-2pts]:" % (format(function), arg_string))
        traceback.print_tb(error.__traceback__)
        print("  %s: %s" % (type(error).__name__, error))
        print()
        return 0

def run_tests(function, examples):
    print("*********** testing %s ***********" % format(function))
    score = 0
    for (arguments, target) in examples:
        score += run_test(function, arguments, target)
    if score == 2*len(examples):
        print("  All tests for %s passed!" % format(function))
    else:
        print("  ^^^")
        print("  Some tests for %s did not pass." % format(function))
    return score


##### Run all tests
test_data = ((
    pad, (
        ((1,), '01'),
        ((12,), '12'),
    )), (
    pad_all, (
        (([1, 2],), ['01', '02']),
        (([1, 22],), ['01', '22']),
    )), (
    initial_board, (
        ((), [2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0]),
    )), (
    is_not_over, (
        (([2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0],), True),
        (([0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2],), True),
        (([0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 10],), False),
    )), (
    valid_moves, (
        ((0, [2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0]), [0, 1, 2, 3, 4]),
        ((1, [2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0]), [6, 7, 8, 9, 10]),
        ((0, [0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2]), [1, 2, 3, 4]),
        ((1, [0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2]), [7, 8, 9, 10]),
    )), (
    mancala_of, (
        ((0,), 5),
    )), (
    pits_of, (
        ((0,), [0, 1, 2, 3, 4]),
    )), (
    player_who_can_do, (
        ((0,), 0),
        ((1,), 0),
        ((4,), 0),
    )), (
    opposite_from, (
        ((0,), 10),
        ((10,), 0),
        ((4,), 6),
        ((6,), 4),
    )), (
    play_turn, (        
        ((0, [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0]), (1, [0, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0])),
        ((4, [2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0]), (1, [2, 2, 2, 2, 0, 1, 3, 2, 2, 2, 2, 0])),
        ((4, [7, 7, 7, 7, 7, 0, 7, 7, 7, 7, 7, 0]), (1, [8, 7, 7, 7, 0, 1, 8, 8, 8, 8, 8, 0])),
        ((4, [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0]), (0, [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0])),
        ((0, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), (1, [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0])),
    )), (
    clear_pits, (
        (([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],), [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]),
        (([1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 5],), [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5]),
    )), (
    is_tied, (
        (([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],), True),
        (([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2],), False),
    )), (
    winner_of, (
        (([0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],), 0),
        (([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2],), 1),
    )), (
    string_of, (
        (([2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0],), '\n           02 02 02 02 02\n        00                00\n           02 02 02 02 02\n'),
        (([1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 4],), '\n           03 03 03 03 03\n        04                02\n           01 01 01 01 01\n'),
        (([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],), '\n           15 14 13 12 11\n        16                10\n           05 06 07 08 09\n'),
    ))
)

total_score = 0
max_possible = 0
for (function, examples) in test_data:
    total_score += run_tests(function, examples)
    max_possible += 2*len(examples)

print("")
print("Total score: %d out of %d" % (total_score, max_possible))

