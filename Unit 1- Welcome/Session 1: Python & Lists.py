#Problem 1: Hello World!
# Given the following lines of code, work with your group members to place the lines in order and write and call your first Python function!

# a. print("Hello world!")
# b. def hello_world():
# c. hello_world()

def hello_world():
  print("Hello world!")
hello_world()


#Problem 2: Today's Mood
# The following function uses a variable, mood to print out "Today's mood: 😎". Copy this code to your Replit and update the mood variable to print out your mood for today.

def todays_mood():
    mood = "😭😻💀" #change this line 
    print("Today's mood: " + mood)
todays_mood()


#Problem 3: Lunch Menu
# The following function accepts one parameter menu. Copy this code to your Replit and add a function call so that "Lunch today is: 🍕" is printed to the console.

def print_menu(menu):
  print("Lunch today is: " + menu)
print_menu("🍕")


#Problem 4: Sum of Two Integers
# The following function returns the sum of two integers: a and b.
# def sum(a, b):
#     return a + b
# Use the sum() function to calculate the sum of 13 and 27. Then, double the calculated sum and print the result to the console.

def sum(a, b):
  return a + b
print(sum(13, 27) * 2)


#Problem 5: Product of Two Integers
# Write a function product() that returns the product of two integers, a and b.

def product(a, b):
  return a*b
print(product(22, 7))


#Problem 6: Classify Age
# Write a function classify_age() that takes an integer age as a parameter and returns "child" if the age is less than 18, and returns "adult" otherwise.

def classify_age(age):
  if age < 18:
    return "child"
  return "adult"
print(classify_age(19))


#Problem 7: What time is it?
# Let's put what we learned in Problems 1-4 all together! Write a function named what_time_is_it() that takes an integer hour as a parameter.
# If hour is 2, the function should return "taco time 🌮".
# If hour is 12, the function should return "peanut butter jelly time 🥪”.
# Otherwise, the function should return "nap time 😴".

def what_time_is_it(hour):
  if hour == 2:
    return "taco time 🌮"
  elif hour == 12:
    return "peanut butter jelly time 🥪"
  return "nap time"
print(what_time_is_it(2))


#Problem 8: Blackjack
# In the game Blackjack, players try to draw a hand of cards that totals as close to 21 as possible. Players "bust" if their cards total more than 21. Players say "Hit me!" if they want the dealer to give them another card.
# Write a function called blackjack() that takes an integer score as a parameter.
# If score equals 21, print "Blackjack!".
# If score is greater than 21, print "Bust!".
# If score is greater than or equal to 17 and less than 21, print "Nice hand!".
# If score is less than 17, print "Hit me!".

def blackjack(score):
  if score == 21:
    print("Blackjack!")
  elif score > 21:
    print("Bust!")
  elif score >= 17 and score < 21:
    print("Nice hand!")
  elif score < 17:
    print("Hit me!")
blackjack(24)
blackjack(19)
blackjack(21)
blackjack(10)


#Problem 9: First Item
# Write a function get_first() that takes in a list as a parameter and returns the first item in the list. Return None if the list is empty.

def get_first(lst):
  if len(lst) == 0:
    return "None"
  return lst[0]
list = [10, 20, 30]
list2 = []
print(get_first(list))
print(get_first(list2))


#Problem 10: Last Item
# Write a function get_last() that takes in a list as a parameter and returns the last item in the list. Return None if the list is empty.

def get_last(lst):
  if len(lst) == 0:
    return "None"
  return lst[len(lst) - 1]
list = [10, 20, 30]
list2 = []
print(get_last(list))
print(get_last(list2))


#Problem 11: Counter
# Write a function counter() that uses the range function to print numbers between 1 and a given stop value (inclusive).

def counter(stop):
  for x in range(1, stop):
    print(x)
counter(7)


#Problem 12: Sum of 1 to 10
# Write a function sum_ten() that returns the sum of numbers from 1 to 10.

def sum_ten():
  result = 0
  for x in range(1, 11):
    result += x
  return result
print(sum_ten())


#Problem 13: Total Sum
# Write a function sum_positive_range() that returns the sum of numbers from 1 to a given stop value (inclusive).

def sum_positive_range(stop):
  result = 0
  for x in range(1, stop + 1):
    result += x
  return result
print(sum_positive_range(6))


#Problem 14: Total Sum in Range
# Write a function sum_range() that returns the sum of numbers from a given start value to a given stop value (inclusive).

def sum_range(start, stop):
def sum_range(start, stop):
  result = 0
  for x in range(start, stop + 1):
    result += x
  return result
print(sum_range(3, 9))


#Problem 15: Negative Numbers
# Write a function print_negatives() that takes a list of integers lst and prints all negative numbers in the list.

def print_negatives(lst):
  for x in lst:
    if x < 0:
      print(x)
print_negatives([3,-2,2,1,-5])