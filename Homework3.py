import re  # importing regex library
# saving the text to the string saveText
saveText='homEwork:\n  tHis iz your homeWork, copy these Text to variable.\n\n\n  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.\n\n\n  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.\n\n\n  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'
saveText = saveText.lower()  # Switching to low case all letters
splittedToLines = saveText.splitlines()  # Splitting the string into separate lines
tempLines = []  # Temporary list for lines
newSentence = []  # Temporary list for the sentence that needs to be added
for line in splittedToLines:  # Iterating through each line in the initial text
    sentences = line.split('.')  # Splitting the line into sentences on dot character
    tempSentences = []  # Temporary list
    for sentence in sentences:  # Iterating through the sentences in each line
        m = re.search(r'\s*(\w*)', sentence)  # Searching for the first word skipping the preceding spaces
        if m != None:  # If word exists (not just new line character)
            tempSentence = re.sub(m.group(1), m.group(1).capitalize(), sentence)  # Assigning capitalized sentence to the temporary variable
            tempSentences.append(tempSentence)  # Adding sentence to the temporary list
        n = re.search(r'\s*(\w+)$', sentence)  # Searching for the end word in each line (paragraph)
        if n != None:  # If word exists (not just new line character)
            newSentence.append(n.group(1))  # Adding the word to the list
    sentences = '.'.join(tempSentences)  # Joining separate capitalized sentences into the line
    tempLines.append(sentences)  # Adding line with capitalized sentences to the temporary variable
    newSentenceString = ' '.join(newSentence)+'.'  # Forming additional sentence
    newSentenceString = newSentenceString.capitalize()  # Capitalizing additional sentence
saveText = '\n'.join(tempLines)  # Re-assembling processed text in the string
saveText = saveText.replace('paragraph.', 'paragraph. ' + newSentenceString)  # Adding the new sentence to the end of specified paragraph
saveText = re.sub(r'(\W+i)z(\W+)', r'\1s\2', saveText)  # Replacing 'iz' with 'is' where needed
print(saveText)  # Output of the resulting text
print('------\nNumber of whitespaces in the text above is: ', len(re.findall(r'\s', saveText)))  # Calculation and output the number of whitespaces





