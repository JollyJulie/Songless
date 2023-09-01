import sqlite3
from datetime import date, datetime, timedelta  # import libraries required for working with date and time
import re
import os
import csv
import pyodbc
from Homework4 import capitalize_line


class Publication:  # parent class for publication
    def __init__(self):
        caption = ''  # String for storing the caption of publication
        text = ''  # String for storing the main text of publication
        customstring = ''  # String for storing the last line of publication
        output = ''  # resulting string for output

    def getdata(self):  # method for getting the data for a publication
        print('Type a text for the publication here:')
        self.text = input()

    def formoutput(self):  # formin output sting for log file
        self.output = ('\n' + self.caption + self.text + '\n' + self.customstring + '\n')

    def writetofile(self):  # wrinting to the log file
        f = open("log.txt", "a")  # open file for adding publication
        f.write(self.output)  # adding publication
        f.close()  # closing file


class News (Publication):  # News class (child for Publication class)
    def __init__(self):
        self.caption = "News -------------\n"

    def getdata(self):  # method for getting all the data extended for a News class
        print('What is the city?')
        self.city = input()
        self.customstring = self.city + ', ' + datetime.now().strftime("%d/%m/%Y %H.%M")
        super(News, self).getdata()


class PrivateAd (Publication):  # PrivateAd class (child for Publication class)
    def __init__(self):
        self.caption = "Private Ad -------------\n"

    def getdata(self):  # method for getting all the data extended for a PrivateAd class
        print('What is the expiration date?')
        year = int(input('Enter a year: '))
        month = int(input('Enter a month: '))
        day = int(input('Enter a day: '))
        self.expirationdate = datetime(year, month, day)
        self.delta = self.expirationdate - datetime.now()
        self.customstring = 'Actual until: ' + self.expirationdate.strftime("%d/%m/%Y") + ', ' + str(self.delta.days) + ' days left'
        super(PrivateAd, self).getdata()


class Necrologue (Publication):  # Necrologue class (child for Publication class)
    def __init__(self):
        self.caption = "Necrologue -----------\n"

    def getdata(self):  # method for getting all the required data extended for a PrivateAd class
        self.deceased = input('What is the name of deceased? ')
        self.customstring = 'In the memory of ' + self.deceased  # Writes "In the memory of <Person>" in the third line of the publication
        super(Necrologue, self).getdata()


class FromTxtFile (Publication):  # Class for providing records from text file
    def __init__(self):
        self.caption = "Record from text file -----------\n"

    def getdata(self):  # method for getting all the required data extended for a FromTxtFile class
        defaultfolder = "C:\\Folder\\"  # Default path is "C:\Folder"
        while True:
            filepath = input('Provide paths to a text file ')  # Getting the path to the file from console
            l = re.search(r'^\w{1}:\\\w+', filepath)  # Searching for full path pattern (starts with a drive letter, followed by ":\")
            if l is None:  # If just a filename (w/o full path)
                filepath = defaultfolder + filepath  # Append default path, otherwise the path is already full
            if os.path.exists(filepath) == False:
                print('Wrong path!\n')
            else:
                break
        f = open(filepath, "r")  # open file for read
        text = f.read()  # reading the context and assigning to text variable
        text = text.lower()  # Coverting to the lower case
        textSplittedToLines = text.splitlines()  # Splitting the text into separate lines (each line is a recordd)
        tempLines = []  # Temporary list for lines
        for line in textSplittedToLines:  # Iterating through each line in the initial text
            line = capitalize_line(line)  # Capitalizing the line
            tempLines.append(line)  # Adding line with capitalized sentences to the temporary variable
        self.text = '\n'.join(tempLines)  # Re-assembling processed text in the string
        # self.text = text
        f.close()  # Closing the file
        os.remove(filepath)  # Deleting the file after processing
        self.customstring = ''  # Writes nothing in the third line of the publication


class Dbconnection:  # Class for work with DB
    def __init__(self):
        self.conn = pyodbc.connect("DRIVER={SQLite3 ODBC Driver};SERVER=localhost;DATABASE=sqlite.db")
        self.cur = self.conn.cursor()

    def insert(self):  # Method for adding the record to DB
        if type(a) is News:  # If a is News object
            self.cur.execute("SELECT * FROM News WHERE city == ? AND text == ?", (a.city, a.text))
            if len(self.cur.fetchall()) == 0:  # If the record doesn't exist already
                self.cur.execute("INSERT INTO News VALUES (?,?,?)", (a.city, a.text, datetime.now()))  # Insert a record
        if type(a) is PrivateAd:
            self.cur.execute("SELECT * FROM PrivateAd WHERE text == ? AND untildate == ?", (a.text, a.expirationdate))
            if len(self.cur.fetchall()) == 0:
                self.cur.execute("INSERT INTO PrivateAd VALUES (?,?,?)", (a.text, a.expirationdate, str(a.delta.days)))
        if type(a) is Necrologue:
            self.cur.execute("SELECT * FROM Necrologue WHERE text == ? AND name == ?", (a.text, a.deceased))
            result = self.cur.fetchall()
            if len(result) == 0:
                self.cur.execute("INSERT INTO Necrologue VALUES (?,?)", (a.text, a.deceased))
        self.cur.commit()
        self.cur.close()
        self.conn.close()


while True:  # A loop for main menu
    print('Select the type of publication:\n1 - News\n2 - Private Advertisement\n3 - Necrologue\n4 - Input from file\n0 - Quit')
    while True:
        userChoice = input()
        if userChoice not in "01234" or len(userChoice) > 1:  # Validation that user entered correct value
            print('Wrong choice, try again!\n')
        else:
            break
    if userChoice == '0':
        break
    elif userChoice == '1':
        a = News()
    elif userChoice == '2':
        a = PrivateAd()
    elif userChoice == '3':
        a = Necrologue()
    elif userChoice == '4':
        a = FromTxtFile()
    a.getdata()  # Get required data
    a.formoutput()  # Form the output string
    a.writetofile()  # Write to a file
    dbcon = Dbconnection()  # Instantiating Dbconnection
    dbcon.insert()  # Adding the record into the DB

    f = open("log.txt", "r")  # open file for read
    text = f.read()  # reading the context and assigning to text variable

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
                writer.writerow({'letter': letter.lower(),
                                 'count_all': letters.count(letter.upper()) + letters.count(letter.lower()),
                                 'count_uppercase': letters.count(letter.upper()), 'percentage': str(
                        100 * (letters.count(letter.upper()) + letters.count(letter.lower())) / len(letters)) + '%'})
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

