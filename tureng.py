import requests
from bs4 import BeautifulSoup as bs4

word = input('Enter Word: ')

translate = requests.get("https://tureng.com/tr/turkce-ingilizce/"+word)
soup = bs4(translate.content, "html.parser")

def wordstr():
    buffer = []
    for tr in soup.find_all('td', 'tr ts'):
        buffer.append(''.join(tr.findAll(text=True)))
    return "\n".join(buffer) 

def wordsen():
    buffer = []
    for en in soup.find_all('td', 'en tm'):
        buffer.append(''.join(en.findAll(text=True)))
    return "\n".join(buffer)

question = input('''\033[36m
1-) Show the Turkish translation
2-) Show the English translation

\033[96mSelect:\033[0m ''')

if question == '1':
    print(f"\033[91m{wordstr()}\033[0m")

elif question == '2':
    print(f"\033[91m{wordsen()}\033[0m")
