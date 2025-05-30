def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    try :
        hrs = float(input("Enter score:"))
    except :
        print("Bad score")
        quit()

    if hrs > 1.0 :
        print("Bad score")
        quit()
    
    if 0.0 <= hrs <= 1.0 :
        if hrs >= 0.9 :
            print("A")
        elif hrs >= 0.8 :
            print("B")
        elif hrs >= 0.7 :
            print("C")
        elif hrs >= 0.6 :
            print ("D")
        elif hrs < 0.6 :
            print("F")

    # end assignment

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
