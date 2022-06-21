from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import webbrowser

def loadMainPage(url):
    global mainSoup
    page = urlopen(Request(url,headers={"User-Agent" :"Mozila/5"}))
    mainSoup = BeautifulSoup(page.read(),'lxml')

def loadpage(url):
    global soup
    page = urlopen(Request(url,headers={"User-Agent" :"Mozila/5"}))
    soup = BeautifulSoup(page.read(),'lxml')
def getDownloadPage(url):
    loadMainPage(url)
    url = mainSoup.find('input',{'name':'FU'}).get('value')
    print(url)
    loadMainPage(url)
def getGDSseason(sn):
    allstrong = soup.findAll('em')
    strong = allstrong
    print(strong)
    for item in allstrong:
        if 'season {}'.format(sn) in str(item).lower():
            print(item.getText(),end=" ")
            strong = allstrong[allstrong.index(item):allstrong.index(item)+3]
            break
        else:
            pass
