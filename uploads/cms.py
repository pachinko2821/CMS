'''
Author: Prajyot M. Chemburkar
Date: 13th June, 2020

provide docx files with name in the format "year-month-day-author-title.txt"
'''

import os
# uses mammoth to extract txt from docx/convert docx to html
import mammoth
# uses docx2txt to extract images
import docx2txt
import datetime
#BeautifulSoup to prettify the html doc
from bs4 import BeautifulSoup as bs
import sqlite3

######################################--Profanity related functions--######################################
# a list of cuss words in hinglish and english
cuss_words = ['aand', 'aandu', 'balatkar', 'beti chod', 'bhadva', 'bhadve', 'bhandve', 'bhootni ke', 'bhosad', 'bhosadi ke', 'boobe', 'chakke', 'chinaal', 'chinki', 'chod',
              'chodu', 'chodu bhagat', 'chooche', 'choochi', 'choot', 'choot ke baal', 'chootia', 'chootiya', 'chuche', 'chuchi', 'chudai khanaa', 'chudan chudai', 'chut',
              'chutad', 'chutadd', 'chutan', 'chutia', 'chutiya', 'gaand', 'gaandfat', 'gaandmasti', 'gaandufad', 'gandu', 'gashti', 'gasti', 'ghassa', 'ghasti', 'harami', 
              'haramzade', 'hawas', 'hijda', 'hijra', 'jhant', 'jhantu', 'kamine', 'kaminey', 'kanjar', 'kutta', 'kamina', 'kuttiya', 'loda', 'lodu', 'lund', 'lundtopi', 
              'lundure', 'maal', 'madarchod', 'mooh mein le', 'mutth', 'najayaz', 'paki', 'raand', 'randi', 'sala', 'saala', 'sali', 'kutti', 'saala', 'saali', 'suar', 
              'tatte', 'tatti', 'teri maa ka', 'bhosada', 'teri maa ki', 'tharak', 'tharki4r5e', '5h1t', '5hit', 'a55', 'anal', 'anus', 'ar5e', 'arrse', 'arse', 'ass',
              'ass-fucker', 'asses', 'assfucker', 'assfukka', 'asshole', 'assholes', 'asswhole', 'a_s_s', 'b!tch', 'b00bs', 'b17ch', 'b1tch', 'ballbag', 'balls', 'ballsack', 
              'bastard', 'beastial', 'beastiality', 'bellend', 'bestial', 'bestiality', 'bi+ch', 'biatch', 'bitch', 'bitcher', 'bitchers', 'bitches', 'bitchin', 'bitching',
              'bloody', 'blow job', 'blowjob', 'blowjobs', 'boiolas', 'bollock', 'bollok', 'boner', 'boob', 'boobs', 'booobs', 'boooobs', 'booooobs', 'booooooobs', 'breasts', 
              'buceta', 'bugger', 'bum', 'bunny fucker', 'butt', 'butthole', 'buttmunch', 'buttplug', 'c0ck', 'c0cksucker', 'carpet muncher', 'cawk', 'chink', 'cipa', 'cl1t', 
              'clit', 'clitoris', 'clits', 'cnut', 'cock', 'cock-sucker', 'cockface', 'cockhead', 'cockmunch', 'cockmuncher', 'cocks', 'cocksuck', 'cocksucked', 'cocksucker', 
              'cocksucking', 'cocksucks', 'cocksuka', 'cocksukka', 'cok', 'cokmuncher', 'coksucka', 'coon', 'cox', 'crap', 'cum', 'cummer', 'cumming', 'cums', 'cumshot',
              'cunilingus', 'cunillingus', 'cunnilingus', 'cunt', 'cuntlick', 'cuntlicker', 'cuntlicking', 'cunts', 'cyalis', 'cyberfuc', 'cyberfuck', 'cyberfucked',
              'cyberfucker', 'cyberfuckers', 'cyberfucking', 'd1ck', 'damn', 'dick', 'dickhead', 'dildo', 'dildos', 'dink', 'dinks', 'dirsa', 'dlck', 'dog-fucker', 'doggin', 
              'dogging', 'donkeyribber', 'doosh', 'duche', 'dyke', 'ejaculate', 'ejaculated', 'ejaculates', 'ejaculating', 'ejaculatings', 'ejaculation', 'ejakulate', 'f u c k',
              'f u c k e r', 'f4nny', 'fag', 'fagging', 'faggitt', 'faggot', 'faggs', 'fagot', 'fagots', 'fags', 'fanny', 'fannyflaps', 'fannyfucker', 'fanyy', 'fatass', 'fcuk',
              'fcuker', 'fcuking', 'feck', 'fecker', 'felching', 'fellate', 'fellatio', 'fingerfuck', 'fingerfucked', 'fingerfucker', 'fingerfuckers', 'fingerfucking', 'fingerfucks', 
              'fistfuck', 'fistfucked', 'fistfucker', 'fistfuckers', 'fistfucking', 'fistfuckings', 'fistfucks', 'flange', 'fook', 'fooker', 'fuck', 'fucka', 'fucked', 'fucker', 
              'fuckers', 'fuckhead', 'fuckheads', 'fuckin', 'fucking', 'fuckings', 'fuckingshitmotherfucker', 'fuckme', 'fucks', 'fuckwhit', 'fuckwit', 'fudge packer', 
              'fudgepacker', 'fuk', 'fuker', 'fukker', 'fukkin', 'fuks', 'fukwhit', 'fukwit', 'fux', 'fux0r', 'f_u_c_k', 'gangbang', 'gangbanged', 'gangbangs', 'gaylord', 
              'gaysex', 'goatse', 'God', 'god-dam', 'god-damned', 'goddamn', 'goddamned', 'hardcoresex', 'hell', 'heshe', 'hoar', 'hoare', 'hoer', 'homo', 'hore', 'horniest', 
              'horny', 'hotsex', 'jack-off', 'jackoff', 'jap', 'jerk-off', 'jism', 'jiz', 'jizm', 'jizz', 'kawk', 'knob', 'knobead', 'knobed', 'knobend', 'knobhead', 'knobjocky', 
              'knobjokey', 'kock', 'kondum', 'kondums', 'kum', 'kummer', 'kumming', 'kums', 'kunilingus', 'l3i+ch', 'l3itch', 'labia', 'lmfao', 'lust', 'lusting', 'm0f0', 'm0fo', 
              'm45terbate', 'ma5terb8', 'ma5terbate', 'masochist', 'master-bate', 'masterb8', 'masterbat*', 'masterbat3', 'masterbate', 'masterbation', 'masterbations', 
              'masturbate', 'mo-fo', 'mof0', 'mofo', 'mothafuck', 'mothafucka', 'mothafuckas', 'mothafuckaz', 'mothafucked', 'mothafucker', 'mothafuckers', 'mothafuckin', 
              'mothafucking', 'mothafuckings', 'mothafucks', 'mother fucker', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckers', 'motherfuckin', 'motherfucking', 
              'motherfuckings', 'motherfuckka', 'motherfucks', 'muff', 'mutha', 'muthafecker', 'muthafuckker', 'muther', 'mutherfucker', 'n1gga', 'n1gger', 'nazi', 'nigg3r', 
              'nigg4h', 'nigga', 'niggah', 'niggas', 'niggaz', 'nigger', 'niggers', 'nob', 'nob jokey', 'nobhead', 'nobjocky', 'nobjokey', 'numbnuts', 'nutsack', 'orgasim', 
              'orgasims', 'orgasm', 'orgasms', 'p0rn', 'pawn', 'pecker', 'penis', 'penisfucker', 'phonesex', 'phuck', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 
              'phuks', 'phuq', 'pigfucker', 'pimpis', 'piss', 'pissed', 'pisser', 'pissers', 'pisses', 'pissflaps', 'pissin', 'pissing', 'pissoff', 'poop', 'porn', 'porno', 
              'pornography', 'pornos', 'prick', 'pricks', 'pron', 'pube', 'pusse', 'pussi', 'pussies', 'pussy', 'pussys', 'rectum', 'retard', 'rimjaw', 'rimming', 's hit', 
              's.o.b.', 'sadist', 'schlong', 'screwing', 'scroat', 'scrote', 'scrotum', 'semen', 'sex', 'sh!+', 'sh!t', 'sh1t', 'shag', 'shagger', 'shaggin', 'shagging', 
              'shemale', 'shi+', 'shit', 'shitdick', 'shite', 'shited', 'shitey', 'shitfuck', 'shitfull', 'shithead', 'shiting', 'shitings', 'shits', 'shitted', 'shitter', 
              'shitters', 'shitting', 'shittings', 'shitty', 'skank', 'slut', 'sluts', 'smegma', 'smut', 'snatch', 'son-of-a-bitch', 'spac', 'spunk', 's_h_i_t', 't1tt1e5', 
              't1tties', 'teets', 'teez', 'testical', 'testicle', 'tit', 'titfuck', 'tits', 'titt', 'tittie5', 'tittiefucker', 'titties', 'tittyfuck', 'tittywank', 'titwank', 
              'tosser', 'turd', 'tw4t', 'twat', 'twathead', 'twatty', 'twunt', 'twunter', 'v14gra', 'v1gra', 'vagina', 'viagra', 'vulva', 'w00se', 'wang', 'wank', 'wanker', 
              'wanky', 'whoar', 'whore', 'willies', 'willy', 'xrated']

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
        exit()
    
    small_content = content[:20]
    small_content = small_content.replace("\n", " ")
    small_content += "...."

    flag = 'green' # green by default
    for cuss in cuss_words:
        if cuss in content:
            found_cuss_words.append(cuss) # appends found cuss words to the found_cuss_words list
            flag = 'red' # red if cuss words found 
        
    fdetails = name.split("-")
    year, month, day = fdetails[0], fdetails[1], fdetails[2]
    Date = datetime.date(int(year), int(month), int(day))
    fdetails = [Date, fdetails[3], fdetails[4], small_content]
    return (flag, fdetails) # returns flag along with file details

# prints all found cuss words
def show_cuss_words():
    for cuss in found_cuss_words:
        print(cuss)

######################################--End--######################################


######################################--conversion functions--######################################    
    
'''

#txt2html function converts the file from txt to html, also adds a header/footer
def txt2html(txtfile, header, footer):
    text = open(txtfile, "r") 
    name = os.path.basename(text.name) # gets name of text file
    
    try:
        year, month, day, author, title = name.split('-') # extracts date, author, and title from file name
    except:
        exit()
    
    title = title.strip(".txt") # remove '.txt' from title

    content = text.read()
    #add css links
    links = '<meta charset="utf-8">'
    links += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">'
    links += '<meta name="description" content="">'
    links += '<meta name="author" content="">'
    links += f'<title>{title}</title>'
    links += '<link href="/includes/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">'
    links += '<link href="/includes/vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">'
    links += "<link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>"
    links += "<link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>"
    links += '<link href="/includes/css/clean-blog.min.css" rel="stylesheet">'


    final_content = [] # this list will contain the contents to be added to the html file
    final_content.append("<h1>"+header+"</h1>\n") # add header 
    paragraphs = content.split('\n') # split paragraphs from the list
    
    for group in paragraphs:
        final_content.append("<p>"+group+"</p>\n") # add paragraphs
    
    final_content.append("<h4>"+footer+"</h4>\n") # add footer

    with open("temp_html","w+") as html_file: # create a temp html file, this is difficult to read
        html_file.write(f"<!DOCTYPE html><html><head>{links}</head><body>") #add initial syntax and title
        
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
    
'''


#converts docx file to html
def docx2html(docxfile, header, footer):
    
    with open(docxfile, "rb") as docx_file:
        name = os.path.basename(docx_file.name) # gets name of text file
    
        try:
            year, month, day, author, title = name.split('-') # extracts date, author, and title from file name
        except:
            exit()

        result = mammoth.convert_to_html(docx_file)
        html = result.value

    title = title[:-5] # removes '.docx' from name
    
    os.mkdir(f"../includes/posts/images/{title}")
    docx2txt.process(docxfile, f"../includes/posts/images/{title}/") # extract and save images
    
    #add css links
    links = '<meta charset="utf-8">'
    links += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">'
    links += '<link rel="stylesheet" href="/includes/css/blog-main.css">'
    links += '<link rel="stylesheet" href="/includes/css/blog-content.css">'
    links += '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">'
    links += '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">'
    links += '<script src="/includes/js/includer.js"></script>'
    links += f'<title>{title}</title>'

    #create a temp file, its gonna be difficult to read
    with open("temp_html", "w+") as html_file:
        html_file.write(f"<!DOCTYPE html><html lang='en'><head>{links}</head><body class='bg-dark'>") #add initial syntax and title
        
        html_file.write(f"<div w3-include-html='/includes/php/header.html'></div><div>Author: {author}\nDate: {day}/{month}/{year}<div>") # add author and date
        
        html_file.write(html+"<div w3-include-html='/includes/php/footer.html'></div></html><script>includeHTML();</script>")
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

######################################--Misc functions--######################################

# updatedb fucntion performs all the functions or checking profanity, updating the database
def updatedb(whateverFile): #takes file as an argument
    
    connect = sqlite3.connect("../includes/php/CMS.db")
    cursor = connect.cursor()

    profanity, fdetails = check_profanity(whateverFile) # check txt file for cuss words, returns True if cuss words found and file details regardless
    Date, Author, Title, small_content = fdetails[0], fdetails[1], fdetails[2], fdetails[3] #gets file details to add into database

    #uncomment below line for text files
    #txt2html(whateverFile, "This is a Header", "This is a Footer") # converts txt to html
    #uncomment below line for docx files
    docx2html(whateverFile, "This is a Header", "This is a Footer") # converts docx to html if no cuss words found 

    #inserts file details into the database
    cursor.execute(f"INSERT INTO postDetails(Date, Author, Title, Profanity, small_content) VALUES('{Date}', '{Author}', '{Title}', '{profanity}', '{small_content}');")
    connect.commit()
    connect.close()

#fileMove moves the files for review/approval at admin panel 
def fileMove():
    connect = sqlite3.connect("../includes/php/CMS.db")
    cursor = connect.cursor()
    cursor.execute("SELECT Title, Profanity FROM postDetails")
    result = cursor.fetchall()
    for row in result:
        name, profanity = row
        
        os.replace(f"{name}.html", f"../cmsadmin/{profanity}-posts/{name}.html")

######################################--End--######################################

