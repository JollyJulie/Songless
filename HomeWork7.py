import re
import csv
import os
f = open("log.txt", "r")  # open file for read
text = f.read()  # reading the context and assigning to text variable
# print(text)

letters = re.findall(r'[a-zA-Z]{1}', text)  # Searching for the letters and adding them to the list 'letters'
processed = []
with open('letters.csv', 'w', newline='') as csvfile:
    headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
    writer = csv.DictWriter(csvfile, fieldnames=headers, quoting=csv.QUOTE_ALL)
    writer.writeheader()
for letter in letters:
    if letter.lower() not in processed:
        with open('letters.csv', 'a', newline='') as csvfile:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(csvfile, fieldnames=headers, quoting=csv.QUOTE_ALL)
            writer.writerow({'letter': letter.lower(), 'count_all': letters.count(letter.upper()) + letters.count(letter.lower()), 'count_uppercase':letters.count(letter.upper()), 'percentage':str(100*(letters.count(letter.upper()) + letters.count(letter.lower()))/len(letters))+'%'})
        processed.append(letter.lower())

text = text.lower()
words = re.findall(r'[a-zA-Z\']+', text)  # Searching for the words and adding them to the list 'words'
processed = []
if os.path.exists('words.csv'):
    os.remove('words.csv')
for word in words:
    if word not in processed:
        with open('words.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='-')
            writer.writerow([word, words.count(word)])
        processed.append(word)

