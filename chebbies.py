#ask the user for input in  CHAPO(C) ,RICE (R), UGALI (U)
#ask the user for input in BEANS(B) , NDENGU(N), NYAMA (Y)
print( "Welcome to chebbies!!")
food = input("what will you eat kind sir?")
bill_chapo = 0
bill_rice = 0
bill_ugali = 0
if food == "C":
    bill_chapo = 20
    chapo_ngapi = int(input ("how many chapos do you want?"))
    if chapo_ngapi >= 1:
        bill_chapo *= chapo_ngapi
        kitoweo1 = input("Accompanied by?")
    if kitoweo1 == "B":
        bill_chapo += 40
        print (f"your bill is {bill_chapo}ksh")
    elif kitoweo1 == "N":
        bill_chapo += 50
        print(f"your bill is {bill_chapo}ksh")
    elif kitoweo1 == "Y":
        bill_chapo += 70
        print(f"your bill is {bill_chapo}ksh")
    else:
        print("Please try again in a moment")   
if food == "R":
    bill_rice = 40
    kitoweo2 = input("Accompanied by?")
    if kitoweo2 == "B":
        bill_rice += 40
        print (f"your bill is {bill_rice}ksh")
    elif kitoweo2 == "N":
        bill_rice += 50
        print(f"your bill is {bill_rice}ksh")
    elif kitoweo2 == "Y":
        bill_rice += 70
        print(f"your bill is {bill_rice}ksh")
    else:
        print("Please try again in a moment")
if food == "U":
    bill_ugali = 30
    ugali_ngapi = int(input ("How many ugali do you want?"))
    if ugali_ngapi >= 1:
        bill_ugali *= ugali_ngapi
        kitoweo3 = input("Accompanied by?")
    if kitoweo3 == "B":
        bill_ugali += 40
        print (f"your bill is {bill_ugali}ksh")
    elif kitoweo3 == "N":
        bill_ugali += 50
        print(f"your bill is {bill_ugali}ksh")
    elif kitoweo3 == "Y":
        bill_ugali += 70
        print(f"your bill is {bill_ugali}ksh")
else:
    print("Please try again in a moment")

print ("after payment please confirm Mpesa message with the nearest stuff")
