from movie import mrun,main
from series import srun,seasonwise,epwise
from custom import *

url = input("Enter The MLWBD URL : ")
preferd= input("Manual select or Custom select : " )
if preferd.lower()== "manual" or preferd.lower() == "1" :
    if "season" in url.lower():
        choise = 'series'
    else:
        choise = "movie"
    if choise.lower() == "movie" or choise.lower() =="1":
        mrun.run(url)
    elif choise.lower() == "series" or choise.lower() =="2":

        srun.run(url)
elif preferd.lower() == '2' or preferd.lower() == "custom":
    openbro(url)

