#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    argc = len(argv)

    print("{:d} argument{}".format(argc, 's' if argc != 1 else ''), end='')
    if argc == 0:
        print('.')
    else:
        print(':', end='\n\n')
        for i, arg in enumerate(argv):
            print("{:d}: {}".format(i + 1, arg))
