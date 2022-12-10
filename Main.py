import requests, re
from webbrowser import open_new_tab
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from lxml import html
from os import system


while True:
    url = "https://www.thesaurus.com/browse/"
    urlin = input("Enter word to find:\n- ").strip().lower().replace(" ", "")
    if (len(urlin) == 0): continue

    url += urlin
    req = Request(url)

    fail = False
    for x in range(0, 10):
        if (x == 10):
            fail = True
            break

        try:
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "lxml")
            break

        except: continue

    if (fail == True):
        print("Error 404\n\n")
        continue
	
	#get all links in the box of words (= the words)
    contents = soup.find(class_ = "css-1fsijta eebb9dz0")
    words = []
    takeaway = 0
    #print(str(contents))
    test = contents.findAll('a')
    for item in test:
        words.append(item.get_text())

    word_bank = []
    for item in words:
        if (item != ""):
            word_bank.append(str(item).title())

    print("╔══════════════════════════════════════════════════════════════════\n║ Word: " + str(urlin) + "\n║ Item count: " + str(len(word_bank) - takeaway) + "\n╠══════════════════════════════════════════════════════════════════\n║ " + '\n║ '.join(word_bank) + "\n╚══════════════════════════════════════════════════════════════════")
    input("Press ENTER to Continue...")
    system('cls')
