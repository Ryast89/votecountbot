from bs4 import BeautifulSoup 
import cloudscraper
import time
import easygui

scraper = cloudscraper.create_scraper()
    
URLstart = easygui.enterbox("Enter a link to the thread (from page 2 or after)")
URLstart = URLstart.split("page-",1)[0] 
URLstart = URLstart + "page-"
pageFirst = easygui.integerbox("Enter the page you want the bot to start looking from (this is usually the page with day start on it)")
pageLast = easygui.integerbox("Enter the page you want the bot to stop on (this is usually the last page of the thread)")
while True:
    quotesList = []
    playerName = easygui.enterbox("Enter the name of the player you want to ISO (this is case sensitive)")
    
    for x in range(pageFirst, pageLast + 1): 
        time.sleep(1)
        URL = URLstart + str(x)
        content = scraper.get(URL)
        soup = BeautifulSoup(content.text, 'html.parser')
        rows = soup.find_all('article', {'data-author': playerName})
                
        quotes = soup.findAll('blockquote', {'class': 'bbCodeBlock bbCodeBlock--expandable bbCodeBlock--quote js-expandWatch'})
        for match in quotes:
            match.decompose()
                    
        for row in rows:
            if row:
                message = row.findChild('div', {'class': 'bbWrapper'})
                message = str(message.text)
                if (((message).replace('b\'\\n', "\n")).replace('b\"\\n', "\n").replace("\\n", "\n")).replace("\\xc2\\xa0\n'", "").replace("\\xc2\\xa0\n\"", "").isspace():
                    message = "."
                try:
                    quotesList.append('[QUOTE="' + playerName + ', post: ' + row.get('id')[5:].replace('st-', '') + ', member: 801280"]' + (message.replace("\\n", "\n").replace('\\\'', '\'')) + '[/QUOTE]\n')
                except:
                    quotesList.append('[QUOTE="' + playerName + ', post: ' + row.get('id')[5:].replace('st-', '') +'Quote had an invalid character in it, lol!Ryast' + '[/QUOTE]\n')
                    
    easygui.codebox("List of all quotes by that player in this range:", "ISO", quotesList)
    if easygui.ynbox('Repeat with another player?', 'Title', ('Yes', 'No')) == False:
        break
