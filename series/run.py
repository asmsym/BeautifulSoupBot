import series.epwise
import seasonwise
def run():
    downloadType = input("EP Wise or Season Wise : ")

    if downloadType.lower() =="ep":
        url,choise,season,episode,pixel = epwise.takeInput()
        #epwise.loadMainPage('https://mlwbd.cloud/movie/the-boys-season-3/')
        epwise.getDownloadPage(url)
        epwise.episodeSelect(choise,season,episode,pixel)
    elif downloadType.lower() =="season":
        seasonwise.loadpage('https://songslyric.site/links/625/')

        seasonwise.getGDSseason('1')






