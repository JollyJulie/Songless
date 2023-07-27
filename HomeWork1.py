import random  # importing Random library

randomNumbers = []  # declaring an empty List
for i in range(0, 100):  # iterating through 100 steps in a loop
    n = random.randint(0, 1000)  # assigning a random number from 0 to 1000 to variable n
    randomNumbers.append(n)  # adding n as a new list element
print(randomNumbers)  # output of unsorted list of random numbers
for i in range(0, 99):  # iterating through 99 steps in outer loop
    for j in range(0, 99 - i):  # iterating through 99-i steps in an inner loop
        if randomNumbers[j] > randomNumbers[j + 1]:  # comparing each element with the next one
            temp = randomNumbers[j]  # declaring temporary variable and assigning to it the value of list element
            randomNumbers[j] = randomNumbers[j + 1]  # assigning to the list element the value of the next list element
            randomNumbers[j + 1] = temp  # assigning to the next list element the value of temporary variable

print(randomNumbers)  # output of sorted list of random numbers

evenCount = 0  # Declaring and initializing the variable for accumulating the count of even numbers
evenSum = 0  # Declaring and initializing the variable for accumulating the sum of even numbers
oddCount = 0  # Declaring and initializing the variable for accumulating the count of odd numbers
oddSum = 0  # Declaring and initializing the variable for accumulating the sum of odd numbers

for number in randomNumbers:  # iterating through all elements in the list
    if number % 2 == 1:  # checking if the list element is even or odd number
        oddCount = oddCount + 1  # incrementing the count of odd elements
        oddSum = oddSum + number  # increasing the sum of odd elements by current element value
    else:  # if the list element is even
        evenCount = evenCount + 1  # incrementing the count of even elements
        evenSum = evenSum + number  # increasing the sum of odd elements by current element value

print("Average for odd is:", oddSum // oddCount)  # Output of average integer value for odd list elements
print("Average for even is:", evenSum // evenCount)  # Output of average integer value for even list elements
