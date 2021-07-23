
#LetterCode by Meri Iskali

from LetterCodeLogic import LCL

def main():
    print("Welcome to the LetterCode program")

    choice = getChoice()
    while choice != 0:
        if choice == 1:
            msg = input("Enter your letters to encode: ")
            result = LCL.Encode(msg)
            print("Your encode message is:\n" + result)
        elif choice == 2:
            msg = input("Enter your numbers to decode (separate with commas): ")
            result = LCL.Decode(msg)
            print("Your decode message is:\n" + result)
        else:
            print("Unknown process...")
        print()
        choice = getChoice()
    print("Thanks for using the Letter Code program")


def getChoice():
    c = - 1
    while c < 0 or c > 2:
        try:
            c = int(input("Choice ? (1=Encode, 2=Decode, 0=Quit): "))
            if c < 0 or c > 2:
                print("Unknown game type: 0, 1, or 2 only.")
        except ValueError:
            print("Illegal input: intergers from 0 to 2 only")
            c = -1

    return c

if __name__== "__main__":
    main()
    
          
