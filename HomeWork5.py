from datetime import date, datetime, timedelta  # import libraries required for working with date and time


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
    print('Select the type of publication:\n1 - News\n2 - Private Advertisement\n3 - Necrologue:\n0 - Quit')
    while True:
        userChoice = input()
        if userChoice not in "0123" or len(userChoice) > 1:  # Validation that user entered correct value
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
    a.getdata()  # Get required data
    a.formoutput()  # Form the output string
    a.writetofile()  # Write to a file


# open and read the file after the appending:
# f = open("log.txt", "r")
# print ('========= resulting file ============')
# print(f.read())
