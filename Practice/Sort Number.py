def input_number_check(Index):
    # print("Please input the %s integer you want to sort:", numberIndex)
    if Index == 0:
        numberIndex = "1st"
    elif Index == 1:
        numberIndex = "2nd"
    elif Index == 2:
        numberIndex = "3rd"

    number = input("Please input the %s integer you want to sort:" % numberIndex)
    while not number.isdigit():
        if number == "exit":
            break
        else:
            input("Invalid number, please input the %s number again:" % numberIndex)
    return number


while True:
    l = []
    for i in range(3):
        number = input_number_check(i)
        l.append(number)
    try:
        l.sort()
        print("The sorted numbers list is:", l)

    except:
        pass
