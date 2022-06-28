from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import webbrowser


def loadpage(url):
    global soup
    page = urlopen(Request(url,headers={"User-Agent" :"Mozila/5"}))
    soup = BeautifulSoup(page.read(),'lxml')



def getDownloadPage(url):
    loadpage(url)
    url = soup.find('input',{'name':'FU'}).get('value')
    print(url)
    loadpage(url)


def getGDS(url,p):
    global boabd
    print("Downloading Main Page")
    getDownloadPage(url)
    if p == '720p':
        q="HEVC"
    else:
        q="kibria"
    allstrong = soup.findAll("strong")
    print("Finding Hindi dubbed")
    for item in allstrong:
        if "hindi" in str(item).lower():
            print(item)
            strong = allstrong[allstrong.index(item):allstrong.index(item)+6]
            break

        elif "dual" in str(item).lower():
            print(item)
            strong = allstrong[allstrong.index(item):allstrong.index(item)+6]
            break

        else:
            strong = allstrong
    print("Finding Download link")

    for item in strong:
        if p  in str(item) and q not in str(item):
            ind = strong.index(item)
            if len(strong[ind].findAll('a'))!=0:
                item = item
            else:
                item = strong[ind+1]
            adsgo =item.findAll('a')
            for link in adsgo:
                if "GDS"  in link.getText():
                    adsgolink =link.get('href')
                    loadpage(adsgolink)
                    print(link)
                    break
                elif "GDshare"  in link.getText():
                    adsgolink =link.get('href')
                    loadpage(adsgolink)
                    print(link)
                    break

                elif p in link.getText():
                    adsgolink =link.get('href')
                    loadpage(adsgolink)
                    print(link)
                    break
            break
    boabd =soup.find('input').get('value')
    print(boabd)
    webbrowser.open(boabd)



def getGDrive(url,p):
    getDownloadPage(url)
    global boabd
    if p == '720p':
        q="HEVC"
    else:
        q="kibria"
    allstrong = soup.findAll("strong")
    for item in allstrong:
        if "hindi" in str(item).lower():
            print(item)
            strong = allstrong[allstrong.index(item):allstrong.index(item)+6]

        elif "dual" in str(item).lower():
            print(item)
            strong = allstrong[allstrong.index(item):allstrong.index(item)+6]

        else:
            strong = allstrong

    for item in strong:
        if p  in str(item) and q not in str(item):
            ind = strong.index(item)
            if len(strong[ind].findAll('a'))!=0:
                item = item
            else:
                item = strong[ind+1]
            adsgo =item.findAll('a')
            for link in adsgo:
                if "GDrive1" in link.getText():
                    #print(link)
                    adsgolink =link.get('href')
                    loadpage(adsgolink)
                    break
            break

    if soup.find('input',{"type":"hidden"}):
        global Gdrive
        GDrive = soup.find('input').get('value')
        print(GDrive)
        webbrowser.open(GDrive)















