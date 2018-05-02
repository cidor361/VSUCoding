def Coins():
    while True:
        try:
            Change = int(input("Enter change please: "))
            if Change > 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("Incorrect input data. Please enter again")

    NumOfFifty = 0
    NumOfTen = 0
    NumOfFive = 0
    NumOfOne = 0

    while  Change > 49:
        Change -= 50
        NumOfFifty += 1
    while Change > 9:
        Change -= 10
        NumOfTen += 1
    while Change > 4:
        Change -= 5
        NumOfFive += 1
    while Change > 0:
        Change -= 1
        NumOfOne += 1

    print("Change:")
    if NumOfFifty > 0:
        print (NumOfFifty, "coins of 50 kop.")
    if NumOfTen > 0:
        print(NumOfTen, "coins of 10 kop.")
    if NumOfFive > 0:
        print(NumOfFive, "coins of 5 kop.")
    if NumOfOne > 0 :
        print(NumOfOne, "coins of 1 kop.")

Coins()