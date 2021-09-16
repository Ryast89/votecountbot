from bs4 import BeautifulSoup 
import cloudscraper
import time
import easygui



playerList = []
voteList = []
votesList = []
scraper = cloudscraper.create_scraper()  # returns a CloudflareScraper instance


URLstart = easygui.enterbox("Enter a link to the thread (from page 2 or after)")
URLstart = URLstart.split("page-",1)[0] 
URLstart = URLstart + "page-"
pageFirst = easygui.integerbox("Enter the page you want the bot to start looking from (this is usually the page with day start on it)")
pageLast = easygui.integerbox("Enter the page you want the bot to stop on (this is usually the last page of the thread)")

for x in range(pageFirst, pageLast + 1): 
    print(x)
    time.sleep(1.5)
    URL = URLstart + str(x)
    content = scraper.get(URL)  # => "<!DOCTYPE html><html><head>..."
    soup = BeautifulSoup(content.text, 'html.parser')
    quotes = soup.findAll('blockquote', {'class': 'bbCodeBlock bbCodeBlock--expandable bbCodeBlock--quote js-expandWatch'})
    for match in quotes:
        match.decompose()
    

   
    rows = soup.find_all('div', {'class': 'bbWrapper'}) # Extract and return first occurrence of tr
    for row in rows:
        rowString = str(row.text)
        rowString = rowString.lower()
        if '[/vote]' in rowString and '[vote]' in rowString:
            parent = row.find_parent('article').find_parent('article').get('data-author')
            #print(parent)
            #print(parent + ' voted for ' + ((rowString.split('[vote]'))[1].split('[/vote]')[0]) + ' in post ' + (URL + "#" + row.find_parent('article').find_parent('article').get('id')))
            
            if parent not in playerList:
                #print(parent)
                playerList.append(parent)
                #print(playerList.index(parent))
                voteList.append(((rowString.split('[vote]'))[1].split('[/vote]')[0]))
                
            voteList[playerList.index(parent)] = ((rowString.split('[vote]'))[1].split('[/vote]')[0])

            #print(row.get_text()) # Print row as text
        elif '[/unvote]' in rowString and '[unvote]' in rowString:
            parent = row.find_parent('article').find_parent('article').get('data-author')
            #print(parent)
            
            if parent not in playerList:
                playerList.append(parent)
                voteList.append(((rowString.split('[unvote]'))[1].split('[/unvote]')[0]))
             
            voteList[playerList.index(parent)] = "NOBODY"
            
            
    continue

for i in range(0, len(voteList)):
    print(playerList[i] + ' is voting for ' + voteList[i])
    votesList.append(str(playerList[i] + ' is voting for ' + voteList[i]) + "\n")

easygui.codebox("List of all votes in this range:", "Final VC", votesList)

