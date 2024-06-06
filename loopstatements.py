#1. The Range Riddle


#Objective: The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. You will correct a code snippet, simulate moods for different days, and create a countdown timer.



#Task 1: Every Other Day Write a program that prints each day of the week, but only if that day is on an even index.

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for num in range(0, len(days_of_week), 2):
    print(days_of_week[num])



#2. Loop Condition Logic
#Objective: The aim of this assignment is to explore the importance of the loop condition in while loops. You will create loops with different conditions to see how they influence the behavior of the loop.

#Task 1: Loop Condition Exploration Write a while loop with a condition that will never be true (an infinite loop). Ask the user a question until their answer triggers a break statement (hint: use an if statement to evaluate their answer).

while True:
    user_input = input("is Cheetolini a competent presidential candidate? ")
    if user_input == "no":
        break
    else:
        continue

#Task 2: Conditional Exit Create a while loop that will terminate after 5 iterations, and each iteration you print which iteration it is on. (use a control variable)

iteration = 0
while iteration < 5:
    iteration += 1
    print(f"Iteration {iteration}")


#4. Python's Random Game Night (EXTRA CREDIT)
#Objective: The aim of this assignment is to explore the random package in Python and understand how it can be used with loops to introduce randomness into your programs.

#Task 1: Random Choice Game Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not keep them playing until they guess correctly.

import random  #import random module

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]  #list of fruits
random_fruit = random.choice(fruits)  #randomly select a fruit from the list
user_guess = input("Guess the fruit: ")  #take user's guess

while user_guess != random_fruit:  #while the user's guess is incorrect
    user_guess = input("BZZZZZZTTT! WRONG. Try again: ")  #prompt the user to guess again

print("Ding Ding Ding!")  #print "Correct!" when the user guesses correctly
