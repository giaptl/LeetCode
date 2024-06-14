#Session 1: Dictionaries in Python
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



# Session 2: Dictionaries in Python II
#1
def cast_vote(votes, candidate):
    if (candidate not in votes):
        votes[candidate] = 1
    else:
        votes[candidate] += 1
    return votes
  
#Test
votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)


#2
def common_keys(dict1, dict2):
    common = []
    for keys in dict1:
        if keys in dict2:
            common.append(keys)
    return common
  
#Test
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
'''
Problem 3: Highest Priority Task
Given a dictionary tasks where keys are task names and values are priorities (1-10, where 10 is the highest priority), write a function get_highest_priority_task() that removes the task with the highest priority from the dictionary and returns its name.
If two tasks have the same priority, return the task that comes first in the alphabet.

def get_highest_priority_task(tasks):
  pass
Example Usage:

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)
Example Output:

task2
task4
task3
{"task1": 8, "task5": 7}
'''


#3
def get_highest_priority_task(tasks):
    sortedList = sorted(tasks.items(), key=lambda x: x[1])
    maxValue = max(tasks.values())
    maxValueList = []
        for key,value in sortedList.items():


    for task, priority in reversed(sortedList):
        if priority == maxValue:
            maxValueList.append(task)
            #del tasks[task]
            #return task
        return task
    return sorted(maxValueList)
    #sorted_dict = {key: }
    #for value in sorted(tasks.values()):

#1 sort list by values
#2 add all keys with same highest value into list
#3 we return list sorted by keys

#Test
tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)
perform_task = (get_highest_priority_task(tasks))
print(perform_task)
perform_task = (get_highest_priority_task(tasks))
print(perform_task)
