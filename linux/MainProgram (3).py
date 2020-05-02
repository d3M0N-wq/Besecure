import requests
from datetime import datetime
from bs4 import BeautifulSoup
import numpy as np
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
import re
import string
import pyfiglet

result = pyfiglet.figlet_format("BEsecure", font="5lineoblique")
print(result)

url=input("Input URL:- ")
URL = 'https://www.whois.com/whois/'+url
URL1 = 'https://www.rank2traffic.com/'+url

Count=0

def BlackList():
    File = open("URL", "r")
    Text = File.read()

    Text1 = Text.splitlines()

    if Text1.count(URL) >=1:
        print("Phishing")
    else:
        NintydaysCondition()
def NintydaysCondition():
     try:
            x = requests.get(URL)
            temp  = x.text
            temp1 = temp.splitlines()
            #Updated_Date ="Updated Date"
            Creation_Date="Creation Date"
            Expiration_Date="Registrar Registration"
            count=0
            for t in temp1:
                if t[:13]==Creation_Date:
                 Cdate=t[15:25]
                 count+=1
                if t[:22]==Expiration_Date:
                 Edate=t[40:50]
                 count+=1
                if count==2:
                    break



            ay2=Cdate[5:7]+"/"+Cdate[8:10]+"/"+Cdate[2:4]
            by2=Edate[5:7]+"/"+Edate[8:10]+"/"+Edate[2:4]
            date1 = datetime.strptime(ay2, '%m/%d/%y')
            date2 = datetime.strptime(by2, '%m/%d/%y')
            sudate1 = date1.date()
            sudate2 = date2.date()
            b = sudate1-sudate2
            print(Cdate)
            print(Edate)
            print(abs(b.days),"days")
            if abs(b.days)<90:
                print("Phishing Site")
            else:
                WebScraping()
     except:
            global Count
            Count+=1
            WebScraping()

def WebScraping():
    try:
        Webpage = requests.get(URL1)
        soup = BeautifulSoup(Webpage.content, 'html.parser')

        mydivs = soup.findAll("div", {"class": "col-xs-12 col-md-4"})

        temp = mydivs[0].get_text().splitlines()

        SessionPerMonth = float(temp[11].split()[0])
        PageViewsPerSession = float(temp[35].split()[0])
        SessionDuration = float(temp[44].split(":")[0])
        BounceRate = float(temp[53].split("%")[0])

        print(BounceRate)
        print(SessionDuration)
        print(PageViewsPerSession)
        print(SessionPerMonth)

        if BounceRate >=80 or SessionDuration<=2 or PageViewsPerSession<=1 :
            print("Phishing site")



        else:
            print("HEY")
            URLAnalysis()

        '''
        print("Session per month       -->" + temp[11])
        print("Pages views per session -->" + temp[35])
        print("Session duration    ------>" + temp[44])
        print("Bounce rate           ---->" + temp[53])
        '''

    except:
        global Count
        Count+=1
        URLAnalysis()


def URLAnalysis():

    global Count
    if Count==2:
        print("Phishing Site")
        return
    ##########################################################################
    File = open("URL", "r")
    Text = File.read()

    Text1 = Text.splitlines()

    # Value of the features of URLs
    X1 = []
    Y1 = []

    #print("Phishing site Datasets")

    for t in Text1:

        # F=[ http/https , html extension , length , slashing count , hyphen count , @count , dash count ]
        F = []

        word = t
        if len(word) == 0:
            continue
        # If scheme = http  , then 0
        # If scheme = https , then 1
        URL_Scheme1 = 0
        if word[4] == 's':
            URL_Scheme1 = 1
        F.append(URL_Scheme1)

        # Checking for html extension
        Html_extension1 = 0
        if word[-4:] == "html":
            Html_extension1 = 1
        F.append(Html_extension1)

        # Checking the length
        URL_length1 = len(word)
        F.append(URL_length1)



        # Checking for hyphen
        HyphenCount1 = 0
        AtCount1 = 0
        DashCount1 = 0
        for i in word:
            if i == '-':
                HyphenCount1 += 1
            if i == '@':
                AtCount1 += 1
            if i == '-':
                DashCount1 += 1
        F.append(HyphenCount1)
        F.append(AtCount1)
        F.append(DashCount1)
        print(F)
        X1.append(F)
        Y1.append(1)

    # Showing in graph
    plt.plot(X1, Y1, 'ro', color='blue')

    #########################################################################
    File1 = open("Original.txt", "r")
    T = File1.read()

    T1 = T.splitlines()

    # Value of the features of URLs

    print("Original site Datasets")

    # Value of the features of URLs
    X2 = []
    Y2 = []

    for T2 in T1:

        # F=[ http/https , html extension , length , slashing count , hyphen count , @count , dash count ]
        F = []

        word = T2
        if len(word) == 0:
            continue
        # If scheme = http  , then 0
        # If scheme = https , then 1
        URL_Scheme1 = 0
        if word[4] == 's':
            URL_Scheme1 = 1
        F.append(URL_Scheme1)

        # Checking for html extension
        Html_extension1 = 0
        if word[-4:] == "html":
            Html_extension1 = 1
        F.append(Html_extension1)

        # Checking the length
        URL_length1 = len(word)
        F.append(URL_length1)


        # Checking for hyphen
        HyphenCount1 = 0
        AtCount1 = 0
        DashCount1 = 0
        for i in word:
            if i == '-':
                HyphenCount1 += 1
            if i == '@':
                AtCount1 += 1
            if i == '-':
                DashCount1 += 1
        F.append(HyphenCount1)
        F.append(AtCount1)
        F.append(DashCount1)
        #print(F)
        X1.append(F)
        X2.append(F)
        Y2.append(0)
        Y1.append(0)

    # Showing in graph

    plt.plot(X2, Y2, 'ro', color='red')

    ############################################################################
    print("Predicting the value")

    X = []

    F = []
    # If scheme = http  , then 0
    # If scheme = https , then 1
    URL_Scheme = 0
    if URL[4] == 's':
        URL_Scheme = 1
    F.append(URL_Scheme)

    # Checking for html extension
    Html_extension = 0
    if URL[-4:] == "html":
        Html_extension = 1
    F.append(Html_extension)

    # Checking the length
    URL_length = len(URL)
    F.append(URL_length)



    # Checking for hyphen
    HyphenCount = 0
    AtCount = 0
    DashCount = 0
    for i in URL:
        if i == '-':
            HyphenCount += 1
        if i == '@':
            AtCount += 1
        if i == '-':
            DashCount += 1
    F.append(HyphenCount)
    F.append(AtCount)
    F.append(DashCount)

    X.append(F)
    print("X1-->")
    print(X1)
    print("Y1-->")
    print(Y1)
    print("X--->")
    print(X)
    classifier = LogisticRegression()
    classifier.fit(X1, Y1)

    temp = classifier.predict_proba(X)
    if temp[0][0] > 0.5:
        print("Original Site")
    else:
        print("Suspicious Site")

    if temp[0][0] >= 0.5:
        plt.plot(X, 1 - temp[0][0], 'ro', color='purple')

    elif temp[0][1] >= 0.5:
        plt.plot(X, temp[0][1], 'ro', color='purple')

    for i in range(50):
        plt.plot(i, 0.5, 'ro', color='black')

    plt.show()

BlackList()