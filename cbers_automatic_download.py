import pandas as pd
import urllib
import wget

#file with all urls
file = "cbers.txt"

#opening the file
with open(file,'r') as text_file:
    #reading line by line
    for line in text_file:
        #printing urls
        print(line)
        #downloading each url
        wget.download(line)