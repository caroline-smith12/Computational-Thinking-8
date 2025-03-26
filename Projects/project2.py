# Beginning: create variables
elsa_points = 0
anna_points = 0

# Middle: Ask questions
# Question 1
answer = input("Which season do you like more: A) winter B) fall?     ")
if answer == "A":
    elsa_points += 1
elif answer == "B":
    anna_points += 1


# Question 2
answer = input("Would you rather: A) spend a day with friends and family B) spend the day in bed with a book?     ")
if answer == "A":
    anna_points += 1
elif answer == "B":
    elsa_points += 1


# Question 3
answer = input("Which drink do you prefer: A) blue raspberry slushy B) apple cider?     ")
if answer == "A":
    elsa_points += 1
elif answer == "B":
    anna_points += 1


# Question 4
answer = input("Which song from Frozen do you like the most: A) Love Is An Open Door B) Let it go?     ")
if answer == "A":
    anna_points += 1
elif answer == "B":
    elsa_points += 1


# Question 5 
answer = input("Which bakery item do you prefer: A) cinnamon roll B) blueberry muffin?     ")
if answer == "A":
    anna_points += 1
elif answer == "B":
    elsa_points += 1


# End of quiz:
if anna_points>elsa_points:
    print("You are most like Anna!!")
if elsa_points>anna_points:
    print("You are most like Elsa!!")