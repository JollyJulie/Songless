import random  # importing Random library
import string  # importing String library
import re  # importing Regex library

def create_dict(m):  # creating a dictionary of m elements
    randomdict = {}  # declaring an empty random Dict
    for s in range(m):  # iterating through m steps (number of dict's keys) in a loop
        n = random.randint(0, 100)  # assigning a number from 0 to 100 to variable n to determine dict's key values
        k = random.choice(string.ascii_letters)  # assigning pre-initialized string constant to variable k
        if k in randomdict:  # if such key already added to the dictionary
            s = s-1  # add another step to the loop
        else:  # the key is unique
            randomdict[k] = n  # adding key/value to the dictionary
    return randomdict  # return dictionary


def create_dict_list(y):  # creating a list of y dictionaries
    randomdictlist = []  # declaring an empty List
    for j in range(y):  # iterating through y (number of dictionaries) steps in a loop
        m = random.randint(2, 10)  # assigning a random from 2 to 10 to variable m to determine the number of dict's keys
        randomdict = create_dict(m)  #creating a random dictionary
        randomdictlist.append(randomdict)  # adding randomdict as a new list element
    return randomdictlist  # return list

def key_to_dict (ch):  # function for adding a certain key to the common dict (if exists)
    hit = False  # Declaring boolean variable "hit" to check if the letter was found previously
    duplicate = False  # Declaring boolean variable "duplicate" to check if this letter was found previously
    index = 0  # Declaring and initializing the variable "Index" for saving the number of dict where the key was found
    value = 0  # Declaring and initializing the variable "value" for saving the value of the found key
    for i in range(y):  # iterating through y steps in a loop
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
        if duplicate:  # checking if a key is found in more than one dict
            commonDict[ch+'_'+str(index+1)] = value  # Adding a key with dict number after underlining character with max value
        else:  # Key found only once
            commonDict[ch] = value  # Adding a key


randomdictList = []  # declaring an empty List
y = random.randint(2, 10)  # assigning a random number from 2 to 10 to variable y to determine the number of dicts
randomdictList = create_dict_list(y)  # Creating a list of random dictionaries
print(randomdictList)  # output of the list of random Dicts
commonDict = {}  # declaring an empty common Dict
for ch in string.ascii_letters:  # iterating through all ASCII letters in outer loop
    key_to_dict(ch)  # calling a function for adding a certain key if exists
print(commonDict)  # output of the common Dict

# ---

def capitalize_sentence(sentence):  # Function for capitalizing a sentence
    m = re.search(r'\s*(\w*)', sentence)  # Searching for the first word skipping the preceding spaces
    if m is not None:  # If word exists (not just new line character)
        tempsentence = re.sub(m.group(1), m.group(1).capitalize(), sentence)  # Capitalizing first word in sentence
    return tempsentence  # Returning capitalized sentence


def capitalize_line(line):  # Function for capitalizing a line
    sentences = line.split('.')  # Splitting the line into sentences on dot character
    tempsentences = []  # Temporary list
    for sentence in sentences:  # Iterating through the sentences in each line
        tempsentence = capitalize_sentence(sentence)  # Capitalizing a sentence
        tempsentences.append(tempsentence)  # Appending a sentence to the temporary list
    sentences = '.'.join(tempsentences)  # Joining separate capitalized sentences into the line
    return sentences  # Returning the line of capitalized sentences

def additional_sentence (text):  # Function that returnes additional string
    newsentencelist = re.findall(r'[0-9A-Za-z]+(?=\.)',text)  # List with the last word in each sentence
    newsentence = ' '.join(newsentencelist).capitalize() + '.'  # Assembling into the new sentence
    return newsentence  # Returns new sentence


# saving the text to the string saveText
saveText='homEwork:\n  tHis iz your homeWork, copy these Text to variable.\n\n\n  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.\n\n\n  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.\n\n\n  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'
saveText = saveText.lower()  # Switching to low case all letters
splittedToLines = saveText.splitlines()  # Splitting the string into separate lines
tempLines = []  # Temporary list for lines
for line in splittedToLines:  # Iterating through each line in the initial text
    line = capitalize_line(line)  # Capitalizing the line
    tempLines.append(line)  # Adding line with capitalized sentences to the temporary variable
saveText = '\n'.join(tempLines)  # Re-assembling processed text in the string

saveText = saveText.replace('paragraph.', 'paragraph. ' + additional_sentence(saveText))  # Adding the new sentence to the end of specified paragraph
saveText = re.sub(r'(\s+i)z(\s+)', r'\1s\2', saveText)  # Replacing 'iz' with 'is' where needed
print(saveText)  # Output of the resulting text
print('------\nNumber of whitespaces in the text above is: ', len(re.findall(r'\s', saveText)))  # Calculation and output the number of whitespaces





