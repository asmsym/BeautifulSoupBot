from series.epwise import *
from series.seasonwise import *
##from epwise import *
##from seasonwise import *
def run(url,eors):
##    downloadType =input("EP Wise or Season Wise : ")
    downloadType = eors

    if downloadType.lower() =="ep":
        choise,season,episode,pixel = takeInput() # Take input
        episodeSelect(choise,season,episode,pixel,url) #select episode and download file
    elif downloadType.lower() =="season":
        loadpage('https://songslyric.site/links/625/')
        getGDSseason('1')
##run('https://mlwbd.love/movie/the-boys-season-3/')





