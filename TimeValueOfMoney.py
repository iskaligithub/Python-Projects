import locale
    
def getAmount(prompt):
     a = -1
     while a <= 0:
          try:
               a = float(input(prompt))
               if (a <= 0):
                    print("Positive values only.")
          except ValueError:
               print("Illegal entry: positive numerics only.")
     return a


def getTerm():
     #... final version must validate for > 0 and not crash on illegale input
     t = 0
     while t <= 0:
          try:
               t = int(input("Enter the Term (in months): "))
               if t <= 0:
                    print("Positive values only for term ")
          except ValueError:
               print("Illegal entry: positive integers only.")
     return t 

     
def doPV():
     amt = getAmount("Future amount to be received: ")
     rate = getAmount("Annual Interest Rate (6.55 = 6.4): ")
     while rate < 1.0 or rate > 25.0:
           print ("Rate is out of bounds: 1 to 25 % only.")
           rate = getAmount("Annual Interest Rate (6.5% = 6.5): ")
     term = getTerm()

    #formula requires monthly rate
     morate = rate / 12.0 / 100.0
     pv = amt / ((1+morate) ** term)
     print("An amount in the future of %s" % locale.currency(amt,grouping=True)
           + " discounted at " + str(term) + " months"
           + "{:.2%}".format(rate/100.0)
           + "annually after" + str(term)
           + "months will have a current value of: %s"
                % locale.currency(pv,grouping=True))
     print("That include ans interest discount of %s"
           % locale.currency((amt - pv),grouping=True))
     print()

  
     
def doFV():
     amt = getAmount("Original Deposit: ")
     rate = getAmount("Annual Interest Rate (6.55 = 6.4): ")
     while rate < 1.0 or rate > 25.0:
           print ("Rate is out of bounds: 1 to 25 % only.")
           rate = getAmount("Annual Interest Rate (6.5% = 6.5): ")
     term = getTerm()

    #formula requires monthly rate
     morate = rate / 12.0 / 100.0
     fv = amt * ((1+morate) ** term)
     print("A original deposit of %s" % locale.currency(amt,grouping=True)
           + " earning  "
           + "{:.2%}".format(rate/100.0)
           + "annually after" + str(term)
           + "months will have a final value of: %s"
                % locale.currency(fv,grouping=True))
     print("That include interest earned of %s"
           % locale.currency((fv - amt),grouping=True))
     print()

 
     
def doFVA():
     amt = getAmount("Monthly Deposit: ")
     rate = getAmount("Annual Interest Rate (6.55 = 6.4): ")
     while rate < 1.0 or rate > 25.0:
           print ("Rate is out of bounds: 1 to 25 % only.")
           rate = getAmount("Annual Interest Rate (6.5% = 6.5): ")
     term = getTerm()

    #formula requires monthly rate
     morate = rate / 12.0 / 100.0
     fva = 0.0
     for i in range(0,term):
         intearn = (fva + amt) * morate
         fva += (intearn + amt)
     print("A monthly deposit of %s" % locale.currency(amt,grouping=True)
           + " earning  "
           + "{:.2%}".format(rate/100.0)
           + "annually after" + str(term)
           + "months will have a final value of: %s"
                % locale.currency(fva,grouping=True))
     print("That include interest earned of %s"
           % locale.currency((fva - (amt*term)),grouping=True))
     print()

  

def getChoice():
    c = -1
    while c < 0 or c > 3:
        try:
            c = int(input("Select Operation: (1=PV, 2=FV, 3=FV-Annuity, 0=Quit): "))
            if c < 0 or c > 3:
                print("Unknown operation: 1-3 or zero only.")
        except ValueError:
               print("Illegal input: integers from = to 3 only.")
    return c
     
def main():
     #set the local for use in currency formatting
     result  = locale.setlocale(locale.LC_ALL, '')
     if result == "C" or result.startswith("C/"):
          locale.setlocale(locale.LC_ALL, 'en_US')

     choice = getChoice()
     while choice != 0:
          print()
          if choice == 1:
               doPV()
          elif choice == 2:
               doFV()
          elif choice == 3:
                    doFVA()
          else:
               print("Unknown operation / not yet implemented.\n")

          choice = getChoice()

     print("Thanks for using the Financial Calculator. ")
     
if __name__ == "__main__":
    main()
    
