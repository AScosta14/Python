import math
import random

print("===== WELCOME TO THE GUESS GAME!!! =====")

print("\n")
print("1 - EASY")
print("2 - MEDIUM")
print("3 - HARD")
print("4 - VERY HARD EXTREME")

level = input("\n Choose the level: ")

if (level == '1'):
    print("\n EASY Level choosen")
    rand_number = random.randint(0,10)
    your_number = input("Write what is the random number between 0 and 10: ")

    while (your_number != rand_number):
          if (your_number > rand_number):
              print("\n WRONG, the random number is SMALLER. Try again!")
              your_number = input("Write what is the random number between 0 and 10: ")
          else:
              print("\n WRONG, the random number is HIGHER. Try again!")
              your_number = input("Write what is the random number between 0 and 10: ")

          if (your_number == rand_number):
              print("\n Congratulations!, YOU ARE RIGHT, you won THE GUESS GAME!")

elif (level == '2'):
     print("\n MEDIUM Level choosen")
     rand_number = random.randint(10,100)
     your_number = input("Write what is the random number between 10 and 100: ")

     while (your_number != rand_number):
         if (your_number > rand_number):
             print("\n WRONG, the random number is SMALLER. Try again!")
             your_number = input("Write what is the random number between 10 and 100: ")
         else:
             print("\n WRONG, the random number is HIGHER. Try again!")
             your_number = input("Write what is the random number between 10 and 100: ")

         if (your_number == rand_number):
            print("\n Congratulations!, YOU ARE RIGHT, you won THE GUESS GAME!")

elif (level == '3'):
    print("\n HARD Level choosen")
    rand_number = random.randint(100,1000)
    your_number = input("Write what is the random number between 100 and 1000: ")

    while (your_number != rand_number):
        if (your_number > rand_number):
            print("\n WRONG, the random number is SMALLER. Try again!")
            your_number = input("Write what is the random number between 100 and 1000: ")
        else:
            print("\n WRONG, the random number is HIGHER. Try again!")
            your_number = input("Write what is the random number between 100 and 1000: ")

        if (your_number == rand_number):
            print("\n Congratulations!, YOU ARE RIGHT, you won THE GUESS GAME!")

elif (level == '4'):
    print("\n VERY HARD EXTREME HARD Level choosen")
    rand_number = random.randint(1000,10000)
    your_number = input("Write what is the random number between 1000 and 10000: ")
    Count = 0

    while (your_number != rand_number):
         if (Count > 10):
             print("\n I am sorry, you have exceeded the limit of wrongs, so let's change the random number! \n")
             rand_number = random.randint(1000,10000)
             Count = 0
         if (your_number > rand_number):
             print("\n WRONG, the random number is SMALLER. Try again!")
             Count = Count + 1
             your_number = input("Write what is the random number between 1000 and 10000: ")
         else:
             print("\n WRONG, the random number is HIGHER. Try again!")
             Count = Count + 1
             your_number = input("Write what is the random number between 1000 and 10000: ")

         if (your_number == rand_number):
            print("\n Congratulations!, YOU ARE RIGHT, you won THE GUESS GAME!")

else:
   print("There isn't this level!!")
