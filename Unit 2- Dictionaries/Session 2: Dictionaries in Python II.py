#Problem 1: Cast Vote
# Write a function cast_vote() that records a vote for a candidate in an election. The function accepts a dictionary votes that maps candidates to their current number of votes and a string candidate that represents the candidate the user would like to vote for. If the candidate doesn't exist, add them to the dictionary. The function should return the updated dictionary.

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


#Problem 2: Keys in Common
# Write a function that takes in two dictionaries, dict1 and dict2 and finds all keys common to both dictionaries. The function returns a list of common keys.

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


#Problem 3: Highest Priority Task
# Given a dictionary tasks where keys are task names and values are priorities (1-10, where 10 is the highest priority), write a function get_highest_priority_task() that removes the task with the highest priority from the dictionary and returns its name.
# If two tasks have the same priority, return the task that comes first in the alphabet.

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