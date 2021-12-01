from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
window = Tk()
window.resizable(False, False)
window.geometry("400x400")
window.title("Dice Simulator Game")
window.configure(bg="skyblue")

dice = ['dice_1.png', 'dice_2.png', 'dice_3.png', 'dice_4.png', 'dice_5.png', 'dice_6.png']
img1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
img2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

dice_lb1 = Label(window, image=img1,width=90,height=90,bg="skyblue")
dice_lb2 = Label(window, image=img2,width=90,height=90,bg="skyblue")

def roll():
    img1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    dice_lb1.configure(image=img1)
    dice_lb1.image=img1
    dice_lb1.place(x=50,y=80)
    if(img1=="dice_1.png"):
        print("1")

    img2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    dice_lb2.configure(image=img2)
    dice_lb2.image = img2
    dice_lb2.place(x=230,y=80)

def exit():
    msg = messagebox.askyesno("Confirm", "Are you sure you want to exit ?")
    if (msg == True):
        window.destroy()
    else:
        pass
roll_btn = Button(window,text="Roll Dice !",command=roll,width=15,bg="black",fg="white").place(x=30,y=280)
exit_btn = Button(window,text="Exit",command=exit,width=15,bg="black",fg="white").place(x=230,y=280)
my_lb = Label(window,text="Developed By Akshit Agarwal",bg="skyblue", fg="black",font=("cambria",11,"italic")).place(x=100,y=375)
window.mainloop()