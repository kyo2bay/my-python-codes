from sys import stdin


def main():

    v, t, s, d = [int(x) for x in stdin.readline().rstrip().split()]

    result = "Yes"
    if t * v <= d <= s * v:
        result = "No"

    print(result)


if __name__ == '__main__':
    main()
