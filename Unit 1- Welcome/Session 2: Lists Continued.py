#Problem 1: Print List
# Write a function print_list() that takes in a list lst as a parameter and prints out each item in the list.

def print_list(lst):
  for item in lst:
      print (item)
#Test
lst = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(lst)


#Problem 2: Print Doubled List
# Write a function doubled() that takes in a list of integers lst as a parameter and prints each item in the list multiplied by two.

def doubled(lst):
  lst = [1,2,3]
  for num in lst:
    print(num * 2)
doubled(lst)


#Problem 3: Return Doubled List
# Modify the function doubled() so that instead of printing the items, it returns a new list of the doubled numbers.

def doubled(lst):
  for num in range(0, len(lst)):
    lst[num] = lst[num]*2
  return lst
#Test
lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)


#Problem 4: Flip Signs
# Write a function flip_sign() that takes in a list of integers lst as a parameter and returns a new list where each number in the original list has been multiplied by -1.

def flip_sign(lst):
  for num in range(0, len(lst)):
    lst[num] = lst[num]*-1
  return lst
#Test
lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)


#Problem 5: Max Difference
# Write a function max_difference() that takes in a list of integers lst and returns the difference between the smallest and largest value in the list.

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


#Problem 6: Below Threshold
# Write a function count_less_than() that takes in a list of integers numbers and an integer threshold as parameters and returns the number of items in numbers that are less than threshold.

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


#Problem 7: Evens List
# Write a function get_evens() that takes in a list of integers lst as a parameter and returns a list of all even numbers in the list.

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


#Problem 8: Multiples of Five
# Write a function multiples_of_five() that prints out multiples of 5 between 1 and 100 (inclusive).

def multiples_of_five():
  for num in range(0, 101, 5):
    print(num)
multiples_of_five()


#Problem 9: Divisors
# Write a function find_divisors() that takes in an integer n as a parameter that returns a list of all divisors of n.

def find_divisors(n):
  lst = []
  for i in range (1, n+1):
    if n%i == 0:
      lst.append(i)
  return lst
#Test
lst = find_divisors(6)
print(lst)


#Problem 10: FizzBuzz
# Write a function fizzbuzz() that takes in an integer n as a parameter and prints the numbers from 1 to n.
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.

def fizzbuzz(n):
  for num in range(1, n+1):
    if num % 3 == 0:
      print("fizz")
    elif num % 5 == 0:
      print("buzz")
    else:
      print(num)
fizzbuzz(13)


#Problem 11: Print the Index
# Write a function print_indices() that takes in an integer list lst as a parameter and prints out the index of each item in the given list.
# Use the function range() to loop through the list indices.

def print_indices(lst):
  for num in range(0, len(lst)):
    print(num)
#Test
lst = [5,1,3,8,2]
print_indices(lst)


#Problem 12: Linear Search
# Write a function linear_search() that takes in a list lst and value target as parameters. The function returns the index of target in lst if found. If target is not found in lst, return -1.

def linear_search(lst, target):
  for num in range(0, len(lst)):
    if lst[num] == target:
      return num
  return -1
#Test
lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)