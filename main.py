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

#HAHA at least we almost finished
#Good shit guys!
#while I got you guys I wanted to ask how yall study python for the class?
#tbh ive j been searching things up as i do them ofc
#preciate ittt
#I printed the cheat sheet and I refer to it when doing exercises.