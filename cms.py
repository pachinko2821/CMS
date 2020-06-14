'''
Author: Prajyot M. Chemburkar
Date: 13th June, 2020

provide txt files with name in the format "year-month-day-author-title.txt"
'''

import os
#uses mammoth to convert docx to html
import mammoth 

######################################--Profanity related functions--######################################
# a list of cuss words in hinglish
cuss_words = ['badhir', 'badhirchand', 'bhakland', 'bhadva', 'bhootnika', 'chinaal', 'chutia', 'ghasti',
                'chutiya', 'haraami', 'haraam', 'hijra', 'hijda', 'hinjda', 'jaanvar', 'kutta', 'kutiya',
                'khota', 'auladheen', 'jaat', 'najayaz', 'gandpaidaish', 'saala', 'kutti', 'soover', 'suar',
                'tatti', 'potty', 'bhenchod', 'bahenchod', 'bahanchod', 'bahencho', 'bancho', 'bahenke',
                'laude', 'takke', 'betichod', 'bhaichod', 'bhains', 'jhalla', 'jhant', 'nabaal', 'pissu',
                'kutte', 'maadherchod', 'madarchod', 'padma', 'raand', 'rand', 'jamai', 'randwa', 'randi',
                'bachachod', 'bachichod', 'soower', 'bachchechod', 'pathe', 'banda', 'booblay', 'booby', 'buble',
                'babla', 'bhonsriwala', 'bhonsdiwala', 'bhosadiwala', 'ched', 'chut', 'chod', 'chodu', 'chodra',
                'choochi', 'chuchi', 'gaandu', 'gandu', 'gaand', 'lavda', 'lawda', 'lauda', 'lund', 'balchod',
                'lavander', 'muth', 'maacho', 'mammey', 'tatte', 'toto', 'bhandwe', 'bhosadchod', 'bhosad', 'bumchod',
                'bum', 'bur', 'cunt', 'cuntmama', 'chipkali', 'pasine', 'jhaat', 'chodela', 'bhagatchod', 'chhola',
                'chudai', 'chudaikhana', 'chunni', 'choot', 'bhoot', 'dhakkan', 'bhajiye', 'fateychu', 'gandnatije',
                'lundtopi', 'gaandu', 'gaandfat', 'gaandmasti', 'makhanchudai', 'gaandmarau', 'gandu', 'chaatu', 'beej',
                'choosu', 'fakeerchod', 'lundoos', 'shorba', 'binbheja', 'bhadwe', 'parichod', 'nirodh', 'pucchi', 'baajer',
                'choud', 'bhosda', 'choos', 'maka', 'chinaal', 'gadde', 'joon', 'chullugand', 'doob', 'khatmal',
                'gandkate', 'bambu', 'lassan', 'danda', 'keera', 'keeda', 'hazaarchu', 'paidaishikeeda', 'kali',
                'safaid', 'poot', 'behendi', 'chus', 'machudi', 'chodoonga', 'baapchu', 'laltern', 'suhaagchudai', 'raatchuda',
                'kaalu', 'neech', 'chikna', 'meetha', 'beechka', 'chooche', 'patichod', 'rundi', 'makkhi', 'biwichod',
                'chodhunga', 'haathi', 'kute', 'jhanten', 'kaat', 'gandi', 'gadha', 'bimaar', 'badboodar', 'dum', 'raandsaala',
                'phudi', 'chute', 'kussi', 'khandanchod', 'ghussa', 'maarey', 'chipkili', 'unday', 'budh', 'chaarpai', 'chodun',
                'chatri', 'chode', 'chodho', 'mullekatue', 'mullikatui', 'mullekebaal', 'momedankatue', 'katua', 'chutiyapa', 'bc',
                'mc', 'chudwaya', 'kutton', 'jungli', 'vahiyaat', 'jihadi', 'atankvadi', 'atankwadi', 'aatanki']

#list of found cuss words, gets updated as cuss words are found
found_cuss_words = []

# check_profanity scans the provided file for any cuss words in the list above, sets flag to True if cuss words are found
def check_profanity(data): # data is the contents of the txt file
    flag = False
    print(data)
    for word in cuss_words:
        if word in data:
            found_cuss_words.append(word) # appends found cuss words to the found_cuss_words list
            flag = True # return True if cuss words found 
        
    return flag
# prints all found cuss words
def show_cuss_words():
    print(found_cuss_words)

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

    with open(f"{title}.html","w+") as html_file: # write html file as title.html
        html_file.write(f"<!DOCTYPE html>\n<html>\n<head>\n<title>{title}</title>\n</head>\n<body>\n") #add initial syntax and title
        
        html_file.write(f"<span>\nAuthor: {author}\nDate: {day}/{month}/{year}\n</span>\n") # add author and date
        
        for group in final_content:
            html_file.write(group) # add article content

        html_file.write("</html>")
    print(f"File converted and saved as {title}.html!")
    html_file.close()



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

    with open(f"{title}.html", "w+") as html_file:
        html_file.write(f"<!DOCTYPE html>\n<html>\n<head>\n<title>{title}</title>\n</head>\n<body>\n") #add initial syntax and title
        
        html_file.write(f"<span>\nAuthor: {author}\nDate: {day}/{month}/{year}\n</span>\n") # add author and date
        
        html_file.write(html+"\n</html>")

    print(f"File converted and saved as {title}.html!")
    html_file.close()

######################################--End--######################################