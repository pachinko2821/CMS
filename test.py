# usage

import sqlite3
import sys
from cms import check_profanity, txt2html, show_cuss_words, docx2html

connect = sqlite3.connect("cms.db")
cursor = connect.cursor()

whateverFile = sys.argv[1] # take txt file as argument    


profanity, fdetails = check_profanity(whateverFile) # check txt file for cuss words, returns True if cuss words found and file details regardless
print(fdetails)
Date, Author, Title = fdetails[0], fdetails[1], fdetails[2]

if profanity == False:
    #for text file
    txt2html(whateverFile, "This is a Header", "This is a Footer") # converts txt to html if no cuss words found 
    #for docx file
    #docx2html(whateverFile, "This is a Header", "This is a Footer") # converts docx to html if no cuss words found 

else:
    print("contains inappropriate words!")
    show_cuss_words() # shows all found cuss words 

cursor.execute(f"INSERT INTO postDetails(Date, Author, Title, Profanity) VALUES('{Date}', '{Author}', '{Title}', '{profanity}');")
connect.commit()
connect.close()