import random  # importing Random library
import string  # importing String library

randomdictList = []  # declaring an empty List
y = random.randint(2, 10)  # assigning a random number from 2 to 10 to variable y to determine the number of dicts
for i in range(0, y):  # iterating through y steps in outer loop
    randomDict = {}  # declaring an empty random Dict
    m = random.randint(2, 10)  # assigning a random from 2 to 10 to variable m to determine the number of dict's keys
    for s in range(0, m):  # iterating through m steps (number of dict's keys) in inner loop
        n = random.randint(0, 100)  # assigning a number from 0 to 100 to variable n to determine dict's key values
        k = random.choice(string.ascii_letters)  # assigning pre-initialized string constant to variable k
        randomDict[k] = n  # assigning n to random Dict key
    randomdictList.append(randomDict)  # adding randomDict as a new list element
print(randomdictList)  # output of the list of random Dicts

commonDict = {}  # declaring an empty common Dict
for ch in string.ascii_letters:  # iterating through all ASCII letters in outer loop
    hit = False  # Declaring boolean variable "hit" to check if the letter was found previously
    duplicate = False  # Declaring boolean variable "duplicate" to check if this letter was found previously
    index = 0  # Declaring and initializing the variable "Index" for saving the number of dict where the key was found
    value = 0  # Declaring and initializing the variable "value" for saving the value of the found key
    for i in range(0, y):  # iterating through y steps in inner loop
        if randomdictList[i].get(ch) is not None:  # checking if the dict's key exists
            if not hit:  # checking if the key was not found yet
                index = i  # Assigning i to the variable Index (dict's number i)
                value = randomdictList[i].get(ch)  # Assigning found dict's key value to the variable Value
                hit = True  # Assigning boolean variable "hit" with "True" value (the key was found)
            else:  # checking if the dict's key found earlier
                duplicate = True  # Assigning True to boolean variable "duplicate" (duplicate has been found)
                if value < randomdictList[i].get(ch):  # checking if previously found dict's key value is less than current one
                    value = randomdictList[i].get(ch)  # Assigning the new value to the variable Value (dict's value)
                    index = i  # Assigning i to the variable Index (dict's number)
    if hit:  # checking if the key is found eventually
        if duplicate:  # checking if  key found in more than one dict
            commonDict[ch+'_'+str(index+1)] = value  # Adding key with dict number after underlining character with max value
        else:  # Key found only once
            commonDict[ch] = value  # Adding a key
print(commonDict)  # output of the common Dict

