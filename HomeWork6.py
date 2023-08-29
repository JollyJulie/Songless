from datetime import date, datetime, timedelta  # import libraries required for working with date and time
import re
import os
from datetime import date, datetime, timedelta
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
        city = input()
        self.customstring = city + ', ' + datetime.now().strftime("%d/%m/%Y %H.%M")
        super(News, self).getdata()


class PrivateAd (Publication):  # PrivateAd class (child for Publication class)
    def __init__(self):
        self.caption = "Private Ad -------------\n"


    def getdata(self):  # method for getting all the data extended for a PrivateAd class
        print('What is the expiration date?')
        year = int(input('Enter a year: '))
        month = int(input('Enter a month: '))
        day = int(input('Enter a day: '))
        expirationdate = datetime(year, month, day)
        delta = expirationdate - datetime.now()
        self.customstring = 'Actual until: ' + expirationdate.strftime("%d/%m/%Y") + ', ' + str(delta.days) + ' days left'
        super(PrivateAd, self).getdata()


class Necrologue (Publication):  # Necrologue class (child for Publication class)
    def __init__(self):
        self.caption = "Necrologue -----------\n"


    def getdata(self):  # method for getting all the required data extended for a PrivateAd class
        deceased = input('What is the name of deceased? ')
        self.customstring = 'In the memory of ' + deceased  # Writes "In the memory of <Person>" in the third line of the publication
        super(Necrologue, self).getdata()

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
        a.getdata()
    elif userChoice == '2':
        a = PrivateAd()
        a.getdata()
    elif userChoice == '3':
        a = Necrologue()
        a.getdata()
    elif userChoice == '4':
        defaultfolder = "C:\\Folder\\"  # Default path is "C:\Folder"
        while True:
            filepath = input('Provide path to a text file ')  # Getting the path to the file from console
            l = re.search(r'^\w{1}:\\\w+', filepath)  # Searching for full path pattern (starts with a drive letter, followed by ":\")
            if l is None:  # If just a filename (w/o full path)
                filepath = defaultfolder + filepath  # Append default path, otherwise the path is already full
            if os.path.exists(filepath) == False:
                print('Wrong path!\n')
            else:
                break
        f = open(filepath, "r")  # open file for read
        line = f.read()  # reading the context and assigning to text variable
        line = line.lower()  # Coverting to the lower case
        m = re.search(r'%type:(\w+)%', line)
        # print(m.group(1))
        if m is None:
            print('Wrong format of input file!')
        else:
            if m.group(1) == 'news':
                a = News()
                t = re.search(r'%text:(.+)%', line)
                a.text = capitalize_line(t.group(1))
                c = re.search(r'%city:(.+)%t', line)
                a.city = capitalize_line(c.group(1))
                a.customstring = a.city + ', ' + datetime.now().strftime("%d/%m/%Y %H.%M")
            if m.group(1) == 'privatead':
                a = PrivateAd()
                e = re.search(r'%expiration_date:(.+)%t', line)
                #expirationdate_format = '09/09/23'
                a.expirationdate = datetime.strptime(e.group(1), '%m/%d/%y')
                delta = a.expirationdate - datetime.now()
                t = re.search(r'%text:(.+)%', line)
                a.text = capitalize_line(t.group(1))
                a.customstring = 'Actual until: ' + a.expirationdate.strftime("%d/%m/%Y") + ', ' + str(delta.days) + ' days left'
            if m.group(1) == 'necrologue':
                a = Necrologue()
                n = re.search(r'%name:(.+)%t', line)
                a.deceased = capitalize_line(n.group(1))
                t = re.search(r'%text:(.+)%', line)
                a.text = capitalize_line(t.group(1))
                a.customstring = 'In the memory of ' + a.deceased  # Writes "In the memory of <Person>" in the third line of the publication
        f.close()  # Closing the file
        os.remove(filepath)  # Deleting the file after processing

    a.formoutput()  # Form the output string
    a.writetofile()  # Write to a file
