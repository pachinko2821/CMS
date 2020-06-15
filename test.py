# usage

import sqlite3
import sys
from cms import check_profanity, txt2html, show_cuss_words, docx2html

connect = sqlite3.connect("webpage/includes/cms.db")
cursor = connect.cursor()

whateverFile = sys.argv[1] # take txt file as argument    


profanity, fdetails = check_profanity(whateverFile) # check txt file for cuss words, returns True if cuss words found and file details regardless
Date, Author, Title, small_content = fdetails[0], fdetails[1], fdetails[2], fdetails[3]

#for text file
txt2html(whateverFile, "This is a Header", "This is a Footer") # converts txt to html
# for docx file
#docx2html(whateverFile, "This is a Header", "This is a Footer") # converts docx to html if no cuss words found 
print(small_content)
cursor.execute(f"INSERT INTO postDetails(Date, Author, Title, Profanity, small_content) VALUES('{Date}', '{Author}', '{Title}', '{profanity}', '{small_content}');")
connect.commit()
connect.close()