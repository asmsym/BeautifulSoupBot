from movie.main import *
##from main import *
def run(url,choise,pixel):

    if choise == '1':
        getGDS(url,pixel)
    elif choise == '2':
        getGDrive(url,pixel)

##run('https://mlwbd.cloud/movie/doctor-strange-in-the-multiverse-of-madness-2022/','1','720p')
