#ask on of the customers for the names of people who are involved in the contest
#create a random number within the input of the customer
#from this number the person paying will be the number generated randomly
import random
print ("Welcome to the banker Roullete")
names = input("Please give me the names of the participants")
print (names)
individuals = names.split(", ")
len_individuals = len(individuals)

random_number = random.randint(1, len_individuals - 1)
if len_individuals == 0:
    print ("no user participated")
else:
    payer = str(individuals[random_number])
    print (payer)