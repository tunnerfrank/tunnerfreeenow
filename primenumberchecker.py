#the number inputed by the user has to be more than 1
#if the number is divisible by 1 and itself and is not divisible by any other number
#ask user to give the nimber to be checked
n = int(input("What number do you want us to check"))
#create a function that checkes the number 
def primenumber_checker(number):
    div = number - 1
    is_prime = True
    while div > 1:
        if number % div == 0:
            is_prime = False
        div -= 1
    if is_prime:
        print("prime")
    else:
        print("not prime")
primenumber_checker(number = n)