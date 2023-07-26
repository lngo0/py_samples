if __name__ == '__main__':
    # create the list (2d Array)
    students = []
    # adding logic to the loop
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # update the list
        students.append([name, score])
    # sort the list by score, then by name
    students.sort(key=lambda col: (col[1], col[0]))
    # first value is the lowest
    lowest = second_lowest = students[0][1]
    value_update = 0
    i = 0
    size = len(students)
    # loop through all second_max values in the list
    while i < size:
        if students[i][1] > second_lowest:
            second_lowest = students[i][1]
            value_update += 1
        if value_update == 1:
            print(students[i][0])
        # after finding the second lowest value, we are good
        if lowest != second_lowest and value_update > 1:
            break
        i += 1
