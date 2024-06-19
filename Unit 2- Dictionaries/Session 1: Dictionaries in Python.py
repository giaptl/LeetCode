#1
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

#2
def create_dictionary(keys, values):
  my_dictionary = {}
  for num in range(len(keys)):
    my_dictionary[keys[num]] = values[num]
  return my_dictionary
#Test
keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))

#3
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

#4
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
#Test
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)