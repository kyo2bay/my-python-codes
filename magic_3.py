from sys import stdin


def main():

    n, s, d = [int(x) for x in stdin.readline().rstrip().split()]

    result = "No"
    for _ in range(n):
        x, y = [int(x) for x in stdin.readline().rstrip().split()]
        if x < s and y > d:
            result = "Yes"
            break

    print(result)


if __name__ == '__main__':
    main()
