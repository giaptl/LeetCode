#Problem 1: Subsequence
# Write a function is_subsequence() that takes in a list of integers lst and a list of integers sequence as parameters. Given these two lists, determine whether the sequence list is a subsequence of the lst list. A subsequence of a list is a set of numbers that aren't necessarily adjacent but are in the same relative order as they appear in the list. Return True if sequence is a subsequence, and False otherwise.

def is_subsequence(lst, sequence):
  for num in range(len(lst) - 1):
    for seq in range(len(sequence)-1):
      if lst[num] == sequence[seq] and lst[num+1] == sequence[seq+1]:
        return True
  return False
#Test- True
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))
#Test- False
lst = [5, 1, 22, 25, 6, -1, 8, 10, 12]
sequence = [1, 6, 1, 10, 11, 12]
print(is_subsequence(lst, sequence))


#Problem 2: Create a Dictionary
# Write a function create_dictionary() that takes in a list of keys and a list of values as parameters. The function returns a dictionary where each item in keys is paired with a corresponding item in values.
# keys[i] should be paired with values[i] in the dictionary where 0 <= i <= len(keys). You may assume keys and values are the same length.

def create_dictionary(keys, values):
  my_dictionary = {}
  for num in range(len(keys)):
    my_dictionary[keys[num]] = values[num]
  return my_dictionary
#Test
keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))


#Problem 3: Print Pair
# Write a function print_pair() that takes in a dictionary dictionary and a key target as parameters. The function looks for the target and when found, it prints the key and it's associated value as "Key: <key>" followed by "Value: <value>". If target is not in dictionary, print "That pair does not exist!".

def print_pair(dictionary, target):
  inDictionary = False
  for key, value in dictionary.items():
    if key==target:
      print("Key: ", key)
      print("Value: " + value)
      inDictionary = True
  if not inDictionary:
    print("That pair does not exist!")
#Test
dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")


#4: Problem 4: Keys Versus Values
# Write a function keys_v_values() that takes in a dictionary dictionary whose keys and values are both integers. The function should find the sum of all keys in the dictionary and the sum of all values.
# If the sum of all keys is greater than the sum of all values, the function should return the string "keys".
# If the sum of all values is greater than the sum of all keys, the function should return the string "values".
# If keys and values have equal sums, the function should return the string "balanced".

def keys_v_values(dictionary):
  sumKeys = 0 
  sumVals = 0
  for key, value in dictionary.items():
    sumKeys += key
    sumVals += value
  if sumKeys > sumVals:
    return "keys"
  elif sumVals > sumKeys:
    return "values"
#Test 1
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)
#Test 2
dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)