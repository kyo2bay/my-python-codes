from sys import stdin


def main():

    stdin = open('input.txt')  # 冒頭にこの1行を追加
    a, b = [int(x) for x in stdin.readline().rstrip().split()]

    result = "foo"
    print(result)


if __name__ == '__main__':
    main()
