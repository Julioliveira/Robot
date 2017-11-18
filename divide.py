import sys

OK = 0
WRONG_NUM_ARGS = 10
DIVIDE_BY_ZERO = 11


def main():
  if len(sys.argv) != 3:
    sys.exit(WRONG_NUM_ARGS)
  if float(sys.argv[2]) == 0:
    sys.exit(DIVIDE_BY_ZERO)
  quotient = float(sys.argv[1])/float(sys.argv[2])
  print '%3.1f' % quotient


if __name__ == '__main__':
    main()