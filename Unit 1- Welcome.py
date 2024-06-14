#Session 1: Python & Lists

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



#Session 2: Lists Continued

#1
def print_list(lst):
  for item in lst:
      print (item)
#Test
lst = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(lst)

#2
def doubled(lst):
  lst = [1,2,3]
  for num in lst:
    print(num * 2)
doubled(lst)

#3
def doubled(lst):
  for num in range(0, len(lst)):
    lst[num] = lst[num]*2
  return lst
#Test
lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)

#4
def flip_sign(lst):
  for num in range(0, len(lst)):
    lst[num] = lst[num]*-1
  return lst
#Test
lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)

#5
def max_difference(lst):
  max = lst[0]
  min = lst[0]
  for num in range(1, len(lst)):
    if lst[num]<min :
      min = lst[num]
    elif lst[num]>max :
      max = lst[num]
  return max-min
#Test
lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)

#6
def count_less_than(numbers, threshold):
  sum = 0
  for i in range (0,len(numbers)):
    if numbers[i] < threshold:
      sum += 1
  return sum
#Test
numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)

#7
def get_evens(lst):
  evenList = []
  for num in range(0, len(lst)):
    if lst[num] % 2 == 0:
      evenList.append(lst[num])
  return evenList
#Test
lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)

#8
def multiples_of_five():
  for num in range(0, 101, 5):
    print(num)
multiples_of_five()

#9
def find_divisors(n):
  lst = []
  for i in range (1, n+1):
    if n%i == 0:
      lst.append(i)
  return lst
#Test
lst = find_divisors(6)
print(lst)

#10
def fizzbuzz(n):
  for num in range(1, n+1):
    if num % 3 == 0:
      print("fizz")
    elif num % 5 == 0:
      print("buzz")
    else:
      print(num)
fizzbuzz(13)

#11
def print_indices(lst):
  for num in range(0, len(lst)):
    print(num)
#Test
lst = [5,1,3,8,2]
print_indices(lst)

#12
def linear_search(lst, target):
  for num in range(0, len(lst)):
    if lst[num] == target:
      return num
  return -1
#Test
lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)
