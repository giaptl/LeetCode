#1
def hello_world():
  print("Hello world!")
hello_world()

#2
def todays_mood():
    mood = "😭😻💀" #change this line 
    print("Today's mood: " + mood)

todays_mood()

#3
def print_menu(menu):
  print("Lunch today is: " + menu)
print_menu("🍕")

#4
def sum(a, b):
  return a + b
print(sum(13, 27) * 2)

#5
def product(a, b):
  return a*b
print(product(22, 7))

#6
def classify_age(age):
  if age < 18:
    return "child"
  return "adult"
print(classify_age(19))

#7
def what_time_is_it(hour):
  if hour == 2:
    return "taco time 🌮"
  elif hour == 12:
    return "peanut butter jelly time 🥪"
  return "nap time"
print(what_time_is_it(2))

#8
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

#9
def get_first(lst):
  if len(lst) == 0:
    return "None"
  return lst[0]
list = [10, 20, 30]
list2 = []
print(get_first(list))
print(get_first(list2))

#10
def get_last(lst):
  if len(lst) == 0:
    return "None"
  return lst[len(lst) - 1]
list = [10, 20, 30]
list2 = []
print(get_last(list))
print(get_last(list2))

#11
def counter(stop):
  for x in range(1, stop):
    print(x)
counter(7)

#12
def sum_ten():
  result = 0
  for x in range(1, 11):
    result += x
  return result
print(sum_ten())

#13
def sum_positive_range(stop):
  result = 0
  for x in range(1, stop + 1):
    result += x
  return result
print(sum_positive_range(6))

#14
def sum_range(start, stop):
  result = 0
  for x in range(start, stop + 1):
    result += x
  return result
print(sum_range(3, 9))

#15
def print_negatives(lst):
  for x in lst:
    if x < 0:
      print(x)
print_negatives([3,-2,2,1,-5])