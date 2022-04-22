import sys
import argparse


# Сначала сделал неименованные аргументы, но нашёл это неудобным и перевёл на именованные
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--rate', required=True, type=int, metavar="Hourly rate")
    parser.add_argument('-hrs', '--hours', required=True, type=int, metavar="Hours reported")
    parser.add_argument('-b', '--bonus', type=int, metavar="Bonus for the period")

    return parser


args = create_parser().parse_args(sys.argv[1:])
print(f"Salary for the employee is {(args.rate * args.hours) + args.bonus}")
