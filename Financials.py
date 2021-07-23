#Financials .... by Meri Iskali

import locale
from Annuity import Annuity
from Loan import Loan
from FutureValue import FutureValue


def getChoice():
    goodVal = False
    while not goodVal:
        try:
            choice = int(input("Select Operation: 1=Annuity, 2=Loan, 3=FutureValue, 0=Quit): "))
            if choice < 0 or choice > 3:
                print("Unknown operation: 1, 2, 3, or 0 only.")
            else:
                goodVal = True
        except ValueError:
            print("Illegal input: integers 0 to 3 only")
    return choice

def getValue(prompt,vType):
    #vType is 'i' integer is wanted 'f is wanted
    goodVal = False
    while not goodVal:
        try:
            if vType.lower() == "i":
                amt = int(input(prompt))
            else:
                amt = float(input(prompt))
            goodVal = True
        except ValueError as ex:
            print("Illegal value: " + str(ex))
            goodVal = False
    return amt

def doAnnuity():
    amt = getValue("Monthly Deposit: ", "f")
    rate = getValue("Annual Interest rate (6.5%=6.5): ","d")
    term = getValue("Term (in months): ","i")
    ann = Annuity(amt, rate, term)
    if ann.isValid():
        print("A monthly deposit of %s" % locale.currency(ann.getAmt(),grouping = True)
              + " earning "
              + "{:.2%}".format(ann.getRate()/100)
              + " annually after "
              + str(ann.getTerm()) + " months will have a final value of %s "
              % locale.currency(ann.getFVA(),grouping=True))
        print("That includes interest earned of: %s"
              % locale.currency(ann.getInterest(),grouping=True))
        sched=input("Full Sched? (Y/N): ")
        if len(sched) >  0 and sched[0].upper() == "Y":
            print("Month     Beg.Bal.     Pmt     Int.Earned       End.Bal.")
            for i in range(1,ann.getTerm()+1):
                print("{:4} {:12,.2f} {:12,.2f} {:12,.2f} {:15,.2f}".format(i, ann.getBegBal[, ann.getAmt(), ann.getIntEarn(i), ann.getEndBal(i)))
    else:
        print("Annuity error: " + ann.getError())
        


def doLoan():
    amt = getValue("Loan Amount: ", "f")
    rate = getValue("Annual Interest rate (6.5%=6.5): ","d")
    term = getValue("Term (in months): ","i")
    lo = Loan(amt, rate, term)
    if lo.isValid():
        print("A Loan of %s" % locale.currency(lo.getAmt(),grouping = True)
              + " charging "
              + "{:.2%}".format(lo.getRate()/100)
              +  " annually with a term of "
              + str(lo.getTerm())
              + " months will require a payment of %s"
              % locale.currency(lo.getMoPmt(),grouping=True))
        print("That includes interest earned of: %s"
              % locale.currency(lo.getInterest(),grouping=True))
        sched=input("Full Sched? (Y/N): ")
        if len(sched) >  0 and sched[0].upper() == "Y":
            print("Month     Beg.Bal.     Pmt     Int.Charged       End.Bal.")
            for i in range(1,lo.getTerm()+1):
                print("{:4} {:12,.2f} {:12,.2f} {:12,.2f} {:15,.2f}".format(i, lo.getBegBal(i), lo.getMoPmt(), lo.getIntChg(i), lo.getEndBal(i)))
    else:
        print("Loan error: " + lo.getError())

def doFutureValue():
    amt = getValue("Loan Deposit: ", "f")
    rate = getValue("Annual Interest rate (6.5%=6.5): ","d")
    term = getValue("Term (in months): ","i")
    fv = FutureValue(amt, rate, term)
    if fv.isValid():
        print("A Loan of %s" % locale.currency(fv.getAmt(),grouping = True)
              + " charging "
              + "{:.2%}".format(fv.getRate()/100)
              + " annually with a term "
              + str(fv.getTerm()) + " months will have require a monthly payment of; %s "
              % locale.currency(fv.getFV(),grouping=True))
        print("That includes interest charges of: %s"
              % locale.currency(fv.getInterest(),grouping=True))
        sched=input("Full Sched? (Y/N): ")
        if len(sched) >  0 and sched[0].upper() == "Y":
            print("Month     Beg.Bal.     Pmt     Int.Charged       End.Bal.")
            for i in range(1,fv.getTerm()+1):
                print("{:4} {:12,.2f} {:12,.2f} {:12,.2f} {:15,.2f}".format(i, fv.getBegBal(i), fv.getAmt(), fv.getIntEarn(i), fv.getEndBal(i)))
    else:
        print("Annuity error: " + fv.getError())

def main():
    result = locale.setlocale(locale.LC_ALL, '')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, 'en_US')
    print("Welcome to the Financials Calculator")

    choice = getChoice()
    while choice != 0:
        if choice == 1:
            doAnnuity()
        elif choice == 2:
            doLoan()
        elif choice == 3:
            doFutureValue()
        else:
            print("Operation unkonwn or not implemented")

        choice = getChoice()
        print()
    print("Thanks for using the Calculator")




if __name__=="__main__":
    main()

    







    
    
