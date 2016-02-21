#!/usr/bin/env python

import argparse
import logging
import re
import sys

DESCRIPTION = """
Python script that implements a Calculator.
Example: python calculator.py 1+2*5-2/1
"""
DEFAULT_ROUNDOFF = 2


def add(x, y):
    return float(x) + float(y)


def sub(x, y):
    return float(x) - float(y)


def mul(x, y):
    return float(x) * float(y)


def div(x, y):
    return float(x) / float(y)


OPERATOR_MAP = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}


def validate_calculation(calculation):
    if not re.match(r'[0-9]', calculation[0]):
        logging.error("Firse entry in the input string '%s' is not a Number."
                      % calculation[0])
        sys.exit(-1)
    if not re.match(r'[0-9]', calculation[-1]):
        logging.error("Last entry in the input string '%s' is not a Number."
                      % calculation[-1])
        sys.exit(-1)


def parse_args():
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('calculation',
                        help="Input string for the calculation.")
    parser.add_argument('-roundoff', default=DEFAULT_ROUNDOFF, type=int,
                        help="Roundoff for the floating point.")
    return parser.parse_args()


def calculator(calculation):
    validate_calculation(calculation)
    last_op = None
    curr_op = None
    calc_str = ''
    ans = 0
    op_count = 0
    for i, item in enumerate(calculation):
        if item in OPERATOR_MAP.keys():
            op_count += 1
            if last_op:
                curr_op = OPERATOR_MAP.get(item)
            else:
                last_op = OPERATOR_MAP.get(item)
            if op_count == 1:  # Handling first occurence of an operator
                ans += float(calc_str)
                calc_str = ''
                continue
        else:
            calc_str += item
        if (last_op and calc_str and curr_op) or (i+1 == len(calculation)):
            ans = last_op(ans, float(calc_str))
            calc_str = ''
            last_op = curr_op
            curr_op = None
    return ans


def main(calculation=None, roundoff=None):
    if calculation is None:
        args = parse_args()
        calculation = args.calculation
        roundoff = args.roundoff
    elif roundoff is None:
        roundoff = DEFAULT_ROUNDOFF
    ans = calculator(calculation)
    logging.info('{entry} = {:.{prec}f}'.format(
        ans, entry=calculation, prec=roundoff))
    return round(ans, roundoff)


def test_calculator():
    assert(main(calculation='1+2*3-4/1') == 5.00)
    assert(main(calculation='22/7.0') == 3.14)
    assert(main(calculation='22/7.0', roundoff=5) == 3.14286)

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                        format='%(asctime)s: %(message)s')
    main()
