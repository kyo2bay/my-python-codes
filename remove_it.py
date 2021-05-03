from sys import stdin


def main():

    _, x = [int(x) for x in stdin.readline().rstrip().split()]
    data = [int(x) for x in stdin.readline().rstrip().split()]

    result = ([y for y in data if y != x])

    if len(result) == 0:
        print()
    else:
        print(*result, sep=' ')


if __name__ == '__main__':
    main()
