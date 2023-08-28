import random  # importing Random library
import string  # importing String library
import re  # importing Regex library


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

if __name__ == '__main__':
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





