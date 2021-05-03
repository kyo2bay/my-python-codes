from sys import stdin


def main():

    stdin = open('input.txt')  # 冒頭にこの1行を追加
    _, m = [int(x) for x in stdin.readline().rstrip().split()]

    dish_condition_list = [[int(x) for x in stdin.readline().rstrip().split()]
                           for _ in range(m)]

    # dish_condition_list = []
    # for _ in range(m):
    #     a, b = [int(x) for x in stdin.readline().rstrip().split()]
    #     dish_condition_list.append([a, b])
    print(dish_condition_list)
    print()

    k = int(stdin.readline().rstrip())
    count = 0

    for _ in range(k):
        c, d = [int(x) for x in stdin.readline().rstrip().split()]
        print(dish_condition_list)
        for x in dish_condition_list:
            if len(list(set(x) & set([c, d]))) > 1:
                count += 1
                print(x)
                dish_condition_list.remove(x)
                break

    print(count)


if __name__ == '__main__':
    main()
