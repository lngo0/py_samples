if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # convert into list
    scores = list(arr)
    # sort the list asc
    scores.sort()
    # set to min value
    first, second = -100, -100

    for score in scores:
        if first < score:
            second = first  # pass value to second
            first = score   # update first's value
    print(second)
