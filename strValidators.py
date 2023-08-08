if __name__ == '__main__':
    s = input()
    alNum = False
    alph = False
    num = False
    lower = False
    upper = False

    for c in s:
        if c.isalnum():
            alNum = True

            if c.isdigit():
                num = True
            else:
                alph = True

                if c.islower():
                    lower = True
                else:
                    upper = True

    print(alNum)
    print(alph)
    print(num)
    print(lower)
    print(upper)
