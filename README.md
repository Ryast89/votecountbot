# votecountbot
Python bot to scrape a xenforo website and gather properly formatted votes for games of mafia, or collect a list of a specific player's posts.

Setup:
1. Download the VCBot.py or isos.py file
2. If you don’t already have python installed, go to python.org/downloads and download the latest Python3 release. You’ll want either the windows 32 bit or 64 bit installer, depending on what you run
3. In the python installer, select “Add Python 3.9 to PATH”, and then click install now
4. Open command prompt. Type “pip help” to see if pip is installed (it should be). If you get a big help message, pip is installed. If not, figure out how to install pip with google
5. You need to install the necessary packages to run the python file. You’ll use pip to install those. In command prompt, run the following commands (and let each one finish before doing the next)
* pip install bs4
* pip install cloudscraper
* pip install easygui
6. You should now be able to change directories to get to your downloads directory. The command “cd downloads” should work
7. Type the command “python VCBot.py” or “python isos.py”. If everything went well, this should run the program.

Some things to try if this fails:
If the file fails to run and you see “ModuleNotFoundError: No module named ‘\_\_\_\_’, then type pip install \_\_\_, where ___ is whichever module you don’t have
If you get “no such file or directory”, then your VCBot file isn’t in downloads. Figure out where it is, then use cd to change to where it is. Using “cd ..” will take you out of whichever directory you are in.
If there’s any other problems, just ask me for how to solve them

Some Other important Information about this program
Don't access the forum while the bot is running, as you may get a too many requests error.
Be ready to wait a few minutes for this to run. It takes a few seconds per page, so if you’re putting it through a 100 page day, it’ll take like 5 minutes to run. Faster than doing it yourself, but if it’s only been a few pages since the last VC, maybe use that instead or just run it on a few pages to find the votes in between.
Once you run the program, the command prompt will output each page it checks, so you get a progress report
There is literally no error checking, if you put something in that the program doesn’t like it will just crash
The bot output is just a list of who everyone is voting for, so you’ll still need to format it into an actual VC yourself
If you want to search for different vote tags (for an event or something), then just open VCBot.py in notepad and change every [vote] and [unvote] to the new tags.
