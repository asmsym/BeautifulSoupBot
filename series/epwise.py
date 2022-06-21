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
    print('Download Page URL :',url)
    loadMainPage(url)
def getGDSep(season,ep,pixel,url):
    getDownloadPage(url)
    allstrong = mainSoup.findAll('strong')
    strong = allstrong
    for item in allstrong:
        if 'ep {}'.format(ep) in str(item).lower() or 'episode {}'.format(ep) in str(item).lower():
            print(item.getText(),end=" ")
            strong = allstrong[allstrong.index(item):allstrong.index(item)+3]
            break
        else:
            pass

    if  strong == allstrong:
        print("Cannot Found The EP {}".format(ep))
        exit()
    for link in strong:
        if pixel in str(link):
##            if link.findAll('a')!=0:
##                link =  strong[strong.index(link)+1]
##            else:
##                link = link
            for href in link.findAll('a'):
                if "GDS"  in href.getText():
                    adsgolink =href.get('href')
                    loadpage(adsgolink)
                    print(href.getText(),end=" ")
                    break
                elif "GDshare"  in href.getText():
                    adsgolink =href.get('href')
                    loadpage(adsgolink)
                    print(href.getText(),end=" ")
                    break

                elif pixel in href.getText():
                    adsgolink =link.get('href')
                    loadpage(adsgolink)
                    print(href.getText(),end=" ")
                    break

            break
    boabd =soup.find('input').get('value')
    print(boabd)
def getGDriveep(season,ep,pixel):

    allstrong = mainSoup.findAll('strong')
    strong = allstrong
    for item in allstrong:
        if 'ep {}'.format(ep) in str(item).lower() or 'episode {}'.format(ep) in str(item).lower():
            print(item.getText(),end=" ")
            strong = allstrong[allstrong.index(item):allstrong.index(item)+3]
            break
        else:
            pass
    for link in strong:
        if pixel in str(link):
##            if link.findAll('a')!=0:
##                link =  strong[strong.index(link)+1]
##            else:
##                link = link
            for href in link.findAll('a'):
                if "GDrive1"  in href.getText():
                    adsgolink =href.get('href')
                    loadpage(adsgolink)
                    print(href.getText(),end=" ")
                    break
                elif "GDrive"  in href.getText():
                    adsgolink =href.get('href')
                    loadpage(adsgolink)
                    print(href.getText(),end=" ")
                    break

                elif pixel in href.getText():
                    adsgolink =link.get('href')
                    loadpage(adsgolink)
                    print(href.getText(),end=" ")
                    break
            break

    try:
        boabd =soup.find('input').get('value')
        print(boabd)
    except AttributeError:
        boabd =adsgolink
        print(boabd)
def GDSorGDrive(choise,season,i,pixel,url):
    if choise=='1':
        getGDSep(season,i,pixel,url)
    elif choise =='2':
        getGDriveep(season,i,pixel,url)

def episodeSelect(choise,season,episode,pixel,url):
    if '-' in episode:
        episodeRange=episode.split("-")
        Start = int(episodeRange[0])
        End= int(episodeRange[1])+1
        for i in range(Start,End):
            GDSorGDrive(choise,season,i,pixel,url)

    elif "," in episode:
        episodeList=episode.split(",")
        for i in episodeList:
            GDSorGDrive(choise,season,i,pixel,url)
    elif "all" in episode.lower():
        for i in range(1,100):
            GDSorGDrive(choise,season,i,pixel,url)
    else:
##        try:
        int(episode)
        GDSorGDrive(choise,season,episode,pixel,url)
##        except:
##            pass
def takeInput():
    #season =input("Enter the season you want to download : ")
    #pixel =input("Enter the pixel size : ")
    pixel = '720p'
    season = '1'
    print("How you want to download your file")
    print("1. GSD")
    print("2. GDrive")
    GDSorGDrive = input("Enter your Choise (GSD or GDrive) : ")
    episode =input("Enter the Episode you want to download : ")
    return GDSorGDrive,season,episode,pixel


##getDownloadPage('https://mlwbd.love/movie/the-boys-season-3/')
##episodeSelect('1','1','2','720p')



