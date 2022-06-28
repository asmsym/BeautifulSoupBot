from tkinter import *
from movie import mrun,main
from series import srun,seasonwise,epwise
from custom import *


def download():
    print("running manual download")
    url = e.get()
    print(url)
    preferd= str(var.get())
#    if  "season" in e.get().lower():
#        preferd ="3"
    choise= str(man.get())
    if preferd =='1':
        if pix.get() ==1:
            pixel = '1080p'
        elif pix.get() ==2:
            pixel = '720p'
        elif pix.get() ==3:
           pixel = 'HVEC 720p '
        elif pix.get() ==4:
           pixel = '480p'
        mrun.run(url,choise,pixel)
    if preferd == '2':
        global myLabel2,e2,getLink
        openbrowser(url)
        myLabel2 = Label(frame,text="Enter your prefered download link")
        myLabel2.grid(row=20,column=1)
        e2 = Entry(frame)
        e2.grid(row=14,column=2)
        getLink = Button(frame,text="Get link!", command=lambda: selecteDownload(e2.get()))
        getLink.grid(row=20,column=3)
    if preferd =="3":
        if eors.get() == 1:
            print("ep")
            if ep.get() ==1:
                print("All episode selected")

            elif ep.get()==2:
                print("Latest episode selected")
        elif eors.get()==2:
            print("season")


def eps():
    global p7,p8
    p7 = Radiobutton(frame,text="all", variable=ep, value=1)
    p8 = Radiobutton(frame,text="latest", variable=ep, value=2)
    p7.grid(row=7,column=3)
    p8.grid(row=8,column=3)
def season():
    try:
        p7.grid_remove()
        p8.grid_remove()
    except:
        pass
    return
def manual():
    removeManual()
    if "season" not in e.get().lower():
        global myLabel, myLabel1, gds, gdrive,p1,p2,p3,p4,p5,p6

        myLabel = Label(frame,text="How do you want to download the file")
        myLabel.grid(row=4,column=2)

        gds = Radiobutton(frame,text="1. GDS", variable=man, value= 1)
        gdrive = Radiobutton(frame,text="2. GDrive",variable=man, value=2)

        gds.grid(row=5,column=2)
        gdrive.grid(row=6,column=2)

        myLabel1 = Label(frame,text="What is the pixel")
        myLabel1.grid(row=7,column=2)

        p1 = Radiobutton(frame,text="1080p", variable=pix, value=1)
        p2 = Radiobutton(frame,text="720p", variable=pix, value=2)
        p3 = Radiobutton(frame,text="720p HVEC", variable=pix, value=3)
        p4 = Radiobutton(frame,text="480p", variable=pix, value=4)
        p1.grid(row=8,column=2)
        p2.grid(row=9,column=2)
        p3.grid(row=10,column=2)
        p4.grid(row=11,column=2)
    elif "season" in e.get().lower():

        p5 = Radiobutton(frame,text="EP", variable=eors, value=1, command= eps )
        p6 = Radiobutton(frame,text="Season", variable=eors, value=2, command = season)
        p5.grid(row=4,column=2)
        p6.grid(row=5,column=2)
        if str(eors.get()) == "1":
            print("Ep")
        elif str(eors.get()) =='2':
            print("season")

def removeManual():
    try:
        myLabel.grid_remove()
        myLabel1.grid_remove()
        p1.grid_remove()
        p2.grid_remove()
        p3.grid_remove()
        p4.grid_remove()
        gds.grid_remove()
        gdrive.grid_remove()
    except:
        pass
    try:
        myLabel2.grid_remove()
        e2.grid_remove()
        getLink.grid_remove()
    except:
        pass
    try:
        p5.grid_remove()
        p6.grid_remove()
    except:
        pass
    try:
        p7.grid_remove()
        p8.grid_remove()
    except:
        pass

def custom():
    removeManual()

    return

# defining Tkinter

root= Tk()
root.title("Py downloader")
root.geometry("500x600")
root.iconbitmap("mlwbd.ico")
#declaring variable
var = IntVar()
man = IntVar()
pix = IntVar()
eors = IntVar()
ep= IntVar()
#creating frame
frame = LabelFrame(root)
frame.pack(fill="both", expand="yes")
infoLabel = Label(frame,text="Etnter the MLWBD Movie or Series link ")
infoLabel.grid(row=1,column=1)
#creating entry point
e = Entry(frame)
e.grid(row=1,column=2)
#creating options
r1 = Radiobutton(frame,text="Manual", variable=var, value=1, command=manual)
r2 = Radiobutton(frame,text="Custom", variable=var, value=2, command=custom)

#Showing options
r1.grid(row=2,column=1)
r2.grid(row=30,column=1)
#submit button
submit=Button(frame,text="Submit",command=lambda: download() )
submit.grid(row=35,column=1)


root.mainloop()
