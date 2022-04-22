import argparse
import itertools
import sys


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', required=True, type=int, metavar="A number to begin with")
    parser.add_argument('-e', '--end', required=True, type=int, metavar="A number to end with")
    return parser


def gen_numbers(from_: int, to: int):
    for num in range(from_, to + 1):
        yield num


args = create_parser().parse_args(sys.argv[1:])
start = int(args.start)
end = int(args.end)

gen = gen_numbers(start, end)
for it in range(start, end + 1):
    print(next(gen))




