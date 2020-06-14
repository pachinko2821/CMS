# usage

import sys
from cms import check_profanity, txt2html, show_cuss_words, docx2html

whateverFile = sys.argv[1] # take txt file as argument    


profanity = check_profanity(whateverFile) # check txt file for cuss words, returns True if cuss words found 


if profanity == False:
    #for text file
    txt2html(whateverFile, "This is a Header", "This is a Footer") # converts txt to html if no cuss words found 
    #for docx file
    docx2html(whateverFile, "This is a Header", "This is a Footer") # converts docx to html if no cuss words found 

else:
    print("contains inappropriate words!")
    show_cuss_words() # shows all found cuss words 