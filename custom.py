from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import webbrowser
from tkinter import *
from time import sleep


def loadMainPage(url):
    global mainSoup
    page = urlopen(Request(url,headers={"User-Agent" :"Mozila/5"}))
    mainSoup = BeautifulSoup(page.read(),'lxml')
def loadpage(url):
    global soup
    page = urlopen(Request(url,headers={"User-Agent" :"Mozila/5"}))
    soup = BeautifulSoup(page.read(),'lxml')
def getDownloadPage(url):
    global durl

    loadMainPage(url)
    durl = mainSoup.find('input',{'name':'FU'}).get('value')
    print('Download Page URL :',durl)
    loadMainPage(durl)


def openbrowser(url):
    getDownloadPage(url)
    webbrowser.open(durl)

def selecteDownload(url):
    adsgolink = url
    print(url)
    loadpage(adsgolink)
    boabd =soup.find('input').get('value')
    webbrowser.open(boabd)


