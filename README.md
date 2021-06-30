# BeSecure (PHISHING WEB-PAGE DETECTION USING ML)

Contributors: Gaurav, Meeraj, Tenzin, Ayush.

There are many approaches or methods to detect any malicious or phishing websites, but since the
implementation is very important, we should make a software that doesn’t need much processing
time, configuration and should be easy to use.
So after considering the above conditions, our group has made an actual Windows supported WebBrowser using C# and a Linux tool with python script running at the background . Our python script
runs whenever a user requests webpage, the code scans the particular page by Web-scraping,
extracting the information about its page based and domain based features from trusted
webservices such as whois and rank2traffic, and blacklisted URLs. Last but not the least, even
further deeper analysis is done using Page URL analysis and the result is predicted using Logistic
Regression.

Linux requirements:-
      python 3.7 or above
      modules:-
      pyfiglet
      requests
      numpy
      bs4
      datetime.
