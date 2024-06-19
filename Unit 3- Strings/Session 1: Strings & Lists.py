# Problem 1: Calling Mississippi
# In a new Replit, copy and paste the following function:
# def count_mississippi(limit):
#     for num in range(1, limit):
#     print( f"{num} mississippi")
# Call the function so that it prints out the following to the console (without calling the function more than once):
# 1 mississipi
# 2 mississipi
# 3 mississipi
# 4 mississipi
# 5 mississipi

def count_mississippi(limit):
  for num in range(1, limit):
    print( f"{num} mississippi")

count_mississippi(6)


# Problem 2: Swap Ends
# Write a function swap_ends() that accepts a string my_str as a parameter and returns a new string where the first and last characters from my_str are swapped.

def swap_ends(my_str):
  firstLetter = my_str[0]
  lastLetter = my_str[len(my_str)-1]
  middleLetters = my_str[1:len(my_str)-1]
  return lastLetter + middleLetters + firstLetter
#Test
my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)


# Problem 3: Is Pangram
# Write a function is_pangram() that takes in a string my_str as a parameter and returns True if the string is a pangram and False if not. A pangram is a sentence containing every letter in the English alphabet.

def is_pangram(my_str):
  alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m", "n","o","p","q","r","s","t","u","v","w","x","y","z"]
  my_str.lower()
  for c in my_str:
    if c in alphabet:
      alphabet.remove(c)
  if len(alphabet) == 0:
    return True
  return False


# Problem 4: Reverse String
# Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.

def reverse_string(my_str):
  reverse = ""
  for c in range(0,len(my_str)):
    reverse = my_str[c] + reverse
  return reverse
#Test
my_str = "live"
print(reverse_string(my_str))


# Problem 5: First Unique
# Write a function first_unique_char() that given a string my_str as a parameter, it finds the first non-repeating character in it and returns its index. If it does not exist, then return -1.

def first_unique_char(my_str):
  for index, letter in enumerate(my_str):
    if my_str.count(letter) == 1:
      return index

  return -1
#Test
my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))


# Problem 6: Minimum Distance
# Write a function min_distance() that takes in a list of strings words and two strings word1 and word2' as parameters. The function should return the minimum distance between word1 and word2 in the list of words. The distance between one word and an adjacent word in the list is 1.

def min_distance(words, word1, word2):
  index1 = words.index(word1)
  index2 = words.index(word2)
  if (index1 == -1) or (index2 == -1):
    return "not found"
  return abs(index2 - index1)
#Test
words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)
words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)