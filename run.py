from movie import mrun,main
from series import srun,seasonwise,epwise

url = input("Enter The MLWBD URL : ")
if "season" in url.lower():
    choise = 'series'
else:
    choise = "movie"
if choise.lower() == "movie" or choise.lower() =="1":
    mrun.run(url)
elif choise.lower() == "series" or choise.lower() =="2":
    srun.run(url)
