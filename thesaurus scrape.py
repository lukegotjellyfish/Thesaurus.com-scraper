import fnmatch
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

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

    links = []
    word_bank = []
    check_start = True
    for link in soup.findAll('a', class_=True, href=True, target=False, id=False):  #get links and filter out unwanted class and target html
        if (check_start == True) and (link.string == "Try Our Apps"): #start
            check_start = False
            continue
        if link.string == "Explore Dictionary.com": #end
            break
        links.append(link.get('href')[8:].title())
    links = links[2:] #remove "dictionary.com"s

    for item in links:
        if (item != ""):
            word_bank.append(item.replace("%20", " "))
    word_bank = sorted(word_bank)

    print("╔══════════════════════\n║ Word: " + str(urlin) + "\n║ Word count: " + str(len(word_bank)) + "\n╠══════════════════════\n║ " + '\n║ '.join(word_bank) + "\n╚══════════════════════")
