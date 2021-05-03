import sys


def are_valid_args(args):

    if len(args) != 3:
        return False

    for i in range(1, 3):
        if not args[i].isdigit():
            return False

    return True


def main(args):

    if not are_valid_args(args):
        print("invalid args")
        sys.exit(1)
    a, b = args[1], args[2]
    print(a, b)


if __name__ == '__main__':
    # main(sys.argv)
    main(['arg,py', '1', '2'])
