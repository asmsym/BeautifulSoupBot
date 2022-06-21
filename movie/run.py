from series.main import *
##from hindi import *
def run():
    url = input("Enter the download url : ")
    print("Choise your setting")
    print("1. Default")
    print("2. Customize")
    choise = input("Enter your choise : ")
    if choise =='2':
        print("How do you want to download the file  ")
        print("1. GDS                          ")
        print("2. GDrive                                ")
        print("Please chose one                      ")
        choise = input("Enter your choise : ")
        pixel = input("Enter your favorit pixel : ")
    else:
        choise = '2'
        pixel ='720p'

    ##url = 'https://mlwbd.cloud/movie/bhool-bhulaiyaa-2-2022/'
    ##pixel ='720p'
    loadpage(url)
    getDownloadPage(url)
    ##getGDS(pixel)
    if choise == '1':
        getGDS(pixel)
    elif choise == '2':
        getGDrive(pixel)


