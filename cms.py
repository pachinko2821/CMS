'''
Author: Prajyot M. Chemburkar
Date: 13th June, 2020

provide txt files with name in the format "year-month-day-author-title.txt"
'''

import os
# uses mammoth to extract txt from docx/convert docx to html
import mammoth 
from bs4 import BeautifulSoup as bs
######################################--Profanity related functions--######################################
# a list of cuss words in hinglish
cuss_words = [' badhir ', ' badhirchand ', ' bhakland ', ' bhadva ', ' bhootnika ', ' chinaal ', ' chutia ', ' ghasti ',
    ' chutiya ', ' haraami ', ' haraam ', ' hijra ', ' hijda ', ' hinjda ', ' jaanvar ', ' kutta ', ' kutiya ', ' khota ', ' auladheen ',
    ' jaat ', ' najayaz ', ' gandpaidaish ', ' saala ', ' kutti ', ' soover ', ' suar ', ' tatti ', ' potty ', ' bhenchod ', ' bahenchod ',
    ' bahanchod ', ' bahencho ', ' bancho ', ' bahenke ', ' laude ', ' takke ', ' betichod ', ' bhaichod ', ' bhains ', ' jhalla ', ' jhant ',
    ' nabaal ', ' pissu ', ' kutte ', ' maadherchod ', ' madarchod ', ' padma ', ' raand ', ' rand ', ' jamai ', ' randwa ', ' randi ',
    ' bachachod ', ' bachichod ', ' soower ', ' bachchechod ', ' pathe ', ' banda ', ' booblay ', ' booby ', ' buble ', ' babla ', ' bhonsriwala ',
    ' bhonsdiwala ', ' bhosadiwala ', ' ched ', ' chut ', ' chod ', ' chodu ', ' chodra ', ' choochi ', ' chuchi ', ' gaandu ',
    ' gandu ', ' gaand ', ' lavda ', ' lawda ', ' lauda ', ' lund ', ' balchod ', ' lavander ', ' muth ', ' maacho ', ' mammey ', ' tatte ',
    ' toto ', ' bhandwe ', ' bhosadchod ', ' bhosad ', ' bumchod ', ' bum ', ' bur ', ' cunt ', ' cuntmama ', ' chipkali ', ' pasine ',
    ' jhaat ', ' chodela ', ' bhagatchod ', ' chhola ', ' chudai ', ' chudaikhana ', ' chunni ', ' choot ', ' bhoot ', ' dhakkan ', ' bhajiye ',
    ' fateychu ', ' gandnatije ', ' lundtopi ', ' gaandu ', ' gaandfat ', ' gaandmasti ', ' makhanchudai ', ' gaandmarau ', ' gandu ', ' chaatu ',
    ' beej ', ' choosu ', ' fakeerchod ', ' lundoos ', ' shorba ', ' binbheja ', ' bhadwe ', ' parichod ', ' nirodh ', ' pucchi ', ' baajer ', ' choud ', 
    ' bhosda ', ' choos ', ' maka ', ' chinaal ', ' gadde ', ' joon ', ' chullugand ', ' doob ', ' khatmal ', ' gandkate ', ' bambu ', ' lassan ', 
    ' danda ', ' keera ', ' keeda ', ' hazaarchu ', ' paidaishikeeda ', ' kali ', ' safaid ', ' poot ', ' behendi ', ' chus ', ' machudi ', 
    ' chodoonga ', ' baapchu ', ' laltern ', ' suhaagchudai ', ' raatchuda ', ' kaalu ', ' neech ', ' chikna ', ' meetha ', ' beechka ', ' chooche ', 
    ' patichod ', ' rundi ', ' makkhi ', ' biwichod ', ' chodhunga ', ' haathi ', ' kute ', ' jhanten ', ' kaat ', ' gandi ', ' gadha ', ' bimaar ', 
    ' badboodar ', ' dum ', ' raandsaala ', ' phudi ', ' chute ', ' kussi ', ' khandanchod ', ' ghussa ', ' maarey ', ' chipkili ', ' unday ', ' budh ', 
    ' chaarpai ', ' chodun ', ' chatri ', ' chode ', ' chodho ', ' mullekatue ', ' mullikatui ', ' mullekebaal ', ' momedankatue ', ' katua ', ' chutiyapa ', 
    ' bc ', ' mc ', ' chudwaya ', ' kutton ', ' jungli ', ' vahiyaat ', ' jihadi ', ' atankvadi ', ' atankwadi ', ' aatanki ']

#list of found cuss words, gets updated as cuss words are found
found_cuss_words = []

# check_profanity scans the provided file for any cuss words in the list above, returns True if cuss words are found
def check_profanity(docfile): 
    #check for file type to extract content to check profanity
    f = open(docfile, "rb")
    name, extension = os.path.splitext(docfile)
    if extension == '.txt':
        f.close()
        f = open(docfile, "r")
        content = f.read()
    elif extension == '.docx':
        result = mammoth.extract_raw_text(f)
        content = result.value
    else:
        print("Unknown File format!\n")
        exit()
    
    flag = False
    print(content)
    for cuss in cuss_words:
        if cuss in content:
            found_cuss_words.append(cuss) # appends found cuss words to the found_cuss_words list
            flag = True # return True if cuss words found 
        
    return flag
# prints all found cuss words
def show_cuss_words():
    for cuss in found_cuss_words:
        print(cuss)

######################################--End--######################################


######################################--txt to html functions--######################################    
    
#txt2html function converts the file from txt to html, also adds a header/footer
def txt2html(txtfile, header, footer):
    text = open(txtfile, "r") 
    name = os.path.basename(text.name) # gets name of text file
    
    try:
        year, month, day, author, title = name.split('-') # extracts date, author, and title from file name
    except:
        print("please keep the file name in format year-month-day-Author-Title.txt")
        exit()
    
    title = title.strip(".txt") # remove '.txt' from title

    content = text.read()

    final_content = [] # this list will contain the contents to be added to the html file
    final_content.append("<h1>"+header+"</h1>\n") # add header 
    paragraphs = content.split('\n') # split paragraphs from the list
    
    for group in paragraphs:
        final_content.append("<p>"+group+"</p>\n") # add paragraphs
    
    final_content.append("<h4>"+footer+"</h4>\n") # add footer

    with open("temp_html","w+") as html_file: # create a temp html file, this is difficult to read
        html_file.write(f"<!DOCTYPE html><html><head>\n<title>{title}</title></head><body>") #add initial syntax and title
        
        html_file.write(f"<span>Author: {author}\nDate: {day}/{month}/{year}</span>") # add author and date
        
        for group in final_content:
            html_file.write(group) # add article content

        html_file.write("</html>")
    
    html_file.close()
        
    # beautify temp file contents and create actual temp file
    with open("temp_html", "r") as html_file:
        with open(f"{title}.html", "w+") as pretty_html_file:    
            content = html_file.read()
            soup = bs(content, 'html.parser')
            content = soup.prettify()
            pretty_html_file.write(content)

        pretty_html_file.close()
    
    html_file.close()

    os.remove("temp_html") # delete temp file
    print(f"File converted and saved as {title}.html!")
    



#converts docx file to html
def docx2html(docxfile, header, footer):
    
    with open(docxfile, "rb") as docx_file:
        name = os.path.basename(docx_file.name) # gets name of text file
    
        try:
            year, month, day, author, title = name.split('-') # extracts date, author, and title from file name
        except:
            print("please keep the file name in format year-month-day-Author-Title.txt")
            exit()
    
    
        result = mammoth.convert_to_html(docx_file)
        html = result.value

    title = title.strip(".docx")

    #create a temp file, its gonna be difficult to read
    with open("temp_html", "w+") as html_file:
        html_file.write(f"<!DOCTYPE html><html><head><title>{title}</title></head><body>") #add initial syntax and title
        
        html_file.write(f"<span>Author: {author}Date: {day}/{month}/{year}</span>") # add author and date
        
        html_file.write(html+"</html>")
    html_file.close()

    #beautify the temp file and create the actual html document
    with open("temp_html", "r") as html_file:
        with open(f"{title}.html", "w+") as pretty_html_file:    
            content = html_file.read()
            soup = bs(content, 'html.parser')
            content = soup.prettify()
            pretty_html_file.write(content)

        pretty_html_file.close()

    #delete the temp file
    os.remove("temp_html")
    print(f"File converted and saved as {title}.html!")
    html_file.close()

######################################--End--######################################