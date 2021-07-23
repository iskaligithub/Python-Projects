#Depreciation .... by Meri Iskali

import locale
from Asset import Asset

def getValue(prompt,vType):
    #vType is 'i' integer is wanted 'f is wanted
    goodVal = False
    while not goodVal:
        try:
            if vType.lower() == "i":
                cost = int(input(prompt))
            else:
                cost = float(input(prompt))
            goodVal = True
        except ValueError as ex:
            print("Illegal value: " + str(ex))
            goodVal = False
    return cost


def doDepreciation():
    cost = getValue("Asset Cost: ", "f")
    salvage = getValue("Salvage Value ","d")
    life = getValue("Life (years): ","i")
    dep = Asset(cost, salvage, life)
    if dep.isValid():
        print("That asset will have an annual depreciation of: %s"
              % locale.currency(dep.getDepreciation(),grouping=True))
        sched=input("Full Sched? (Y/N): ")
        if len(sched) >  0 and sched[0].upper() == "Y":
            print("Year    Beg.Val.     Depreciation       End.Val.")
            for i in range(1,dep.getLife()+1):
                print("{:4} {:12,.2f} {:12,.2f} {:15,.2f}".format(i, dep.getBegVal(i), dep.getDepreciation(), dep.getEndVal(i)))

        else:
            print("Depreciation error: " + dep.getError())

def main():
    result = locale.setlocale(locale.LC_ALL, '')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, 'en_US')
    print("Welcome to the Depreciation Calculator")
    choice = input("Do you have an asset? (Y/N): ")
    while choice != "n":
        if choice == "y":
            doDepreciation()
            choice = input("Do you have an asset? (Y/N): ")
        else:
            print("Operation unkonwn or not implemented")

        print()
    print("Thanks for using the Depreciation Calculator!")



if __name__=="__main__":
    main()
