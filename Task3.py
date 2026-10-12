day = 0

print("Is your birthday in Set1?")
print(" 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31")
answer = int(input("Enter 0 for No and 1 for Yes: "))
if answer == 1:
    day += 1


print("\nIs your birthday in Set2?")
print(" 2  3  6  7 10 11 14 15 18 19 22 23 26 27 30 31")
answer = int(input("Enter 0 for No and 1 for Yes: "))
if answer == 1:
    day += 2


print("\nIs your birthday in Set3?")
print(" 4  5  6  7 12 13 14 15 20 21 22 23 28 29 30 31")
answer = int(input("Enter 0 for No and 1 for Yes: "))
if answer == 1:
    day += 4


print("\nIs your birthday in Set4?")
print(" 8  9 10 11 12 13 14 15 24 25 26 27 28 29 30 31")
answer = int(input("Enter 0 for No and 1 for Yes: "))
if answer == 1:
    day += 8

print("\nIs your birthday in Set5?")
print("16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31")
answer = int(input("Enter 0 for No and 1 for Yes: "))
if answer == 1:
    day += 16

print("\nYour birthday is:", day)
