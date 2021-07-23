#ForeignCurrency written by Meri Iskali.

import locale

rEUR = rGBP = rJPY = rCAD = rRUB = 0.0

def getRates():
    global rEUR, rGBP, rJPY, rCAD, rRUB
    print("Please enter the currency rate per US $\n")
    rEUR = getOneRate("EUR")
    rGBP = getOneRate("GBP")
    rJPY = getOneRate("JPY")
    rCAD = getOneRate("CAD")
    rRUB = getOneRate("RUB")

def getOneRate(prompt):
    a = -1
    while a <= 0:
        try:
            a = float(input(prompt + ": "))
            if (a <= 0):
                print("Positive values only.")
        except ValueError:
               print("Illegal entry: positive numerics only.")
    return a

def getChoice():
    choice = -1
    while choice < 0 or choice > 5:
        try:
            choice = int(input("Currency? (1=EUR,2=GBP,3=JPY,4=CAD,5=RUB,9=New Rates,0=Quit): "))
            if (choice < 0 or choice > 5 and choice != 9):
                print("Unknown operation: (1-5, 9, or 0 only)")
        except ValueError:
            print("Illegal input: intergers 0-5 or 9 only")
    return choice
           
def doValuation():
    global rEUR, rGBP, rJPY, rCAD, rRUB
    qty = 0
    cval = 0.0
    grandtotal = 0.0
    totcunits = [0, 0, 0, 0, 0]
    totcval = [0.0, 0.0, 0.0, 0.0, 0.0]
    totcnames = ["EUR", "GBP", "JPY", "CAD", "RUB"]
    totcnmfull = [ "Euros", "Pounds sterling", "Yen", "Loonie", "Rouble" ]
    crates = [ rEUR, rGBP, rJPY, rCAD, rRUB ]
    
    

    choice = getChoice()
    while choice != 0:
        if choice <= 5:
            qty = getQty(totcnmfull[choice-1])
            cval = qty * crates[choice - 1]
            print(str(qty) + " " + totcnmfull[choice -1] + " has a value of %s "
                  %locale.currency(cval,grouping=True))
            totcunits[choice-1] = totcunits[choice-1] + qty
            totcval[choice-1] = totcval[choice-1] + cval
        
        elif choice == 9:
            choice = getRates()
            crates = [ rEUR, rGBP, rJPY, rCAD, rRUB ]
        else:
            print("Unknown currency of operation")
            
        print()
        choice = getChoice()
    print("Purchase Summary: ")
    grandtot = 0.0
    for i in range(0,5):
        print(totcnames[i] + ": "
              + str(totcunits[i]) + " units for a value of: %s"
                %locale.currency(totcval[i],grouping=True))
        grandtot = grandtot + totcval[i]
    print("The total value of the proposed currency purchases was %s "
          %locale.currency(grandtot,grouping=True))
            
def getQty(prompt):
    q = -1
    #final version must validate and handle exceptions
    while q < 0:
        try:
            q = int(input("How many " + prompt + " are you buying? "))
            if (q < 0):
                print("Input out of bounds: non-negative integers only. ")
        except ValueError:
            print("Illegal input: numeric integers >= 0 only. ")
            q = -1
    return q
    
def main():
    #set the local for use in currency formatting
    result  = locale.setlocale(locale.LC_ALL, '')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, 'en_US')

    print("Welcome to the Foreign Currency Calculator.")

    getRates()
    doValuation()
    
    print("Thanks for using the currency calculator.")
    

if __name__ == "__main__":
    main()
    
