import requests
from datetime import datetime
from bs4 import BeautifulSoup

def inputProcessorAOC(cookieValue,day=(datetime.now()).strftime("%d"),year=(datetime.now()).strftime("%Y")): # Your session cookie, day's date (if blank will default to current), year including century/milenium (if blank will default to current)
    # correctly format day date
    if day[0]=="0":
        day = day[1]
    #create url and cookie
    url = (f"https://adventofcode.com/{year}/day/{day}/input")
    cookies = {"session":cookieValue}
    resp = requests.get(url,cookies=cookies)
    if resp.status_code == 200:
        print("CONNECTED to", url)
        soup = BeautifulSoup(resp.text, 'html.parser')
    else:
        print("ERROR GATHERING URL")
        exit()
    return soup
