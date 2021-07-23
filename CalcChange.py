
def getCoin(coinType):
    c = -1
    while c < 0:
        try :
            c = int(input("How many " + coinType + " do you have? "))
            if (c < 0):
                print("Coin counts cannot be negative. Please re-enter.")
        except ValueError:
            print("Illegal input. Must be non-negative. Please re-enter.")
            c = -1
    return c


print("Welcome to the change Calculator")
print()

grandTot = 0
choice = input("Do you have change (y/n)? ")
while choice.lower() == "y":
    h = getCoin("Half-Dollars")
    q = getCoin("Quarters")
    d = getCoin("Dimes")
    n = getCoin("Nickles")
    p = getCoin("Pennies")
    print()

    totVal = (h*50) + (q*25) + (d*10) + (n*5) + p
    print("You have " + str(totVal) + " cents.")
    dollars = totVal // 100
    cents = totVal % 100
    #grandTot = grandTot + totVal
    grandTot += totVal

    print("Which is " + str(dollars) + " dollars and "
          + str(cents) + " cents.")

    print()

    choice = input("Do you have more change (y/n)? ")
    print()
    
print("You had a total of " + str(grandTot) + " cents.\n" +
      " Which is " + str(grandTot // 100) + " dollars and " + str(grandTot % 100) +
      " cents.")            
print("Thanks for using the change calculator.")


