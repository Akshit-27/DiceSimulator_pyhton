from tkinter import  *
from tkinter import messagebox
# from random import
import random
window = Tk()
window.resizable(False,False)
window.geometry("400x400")
window.title("Dice Simulator Game")
window.configure(bg="skyblue")

dice_lb = Label(window,text="",font="Helvitica,360")
def roll():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    # print(f'{random.choice(dice)}{random.choice(dice)}')
    dice_lb.configure(text=f"{random.choice(dice)}{random.choice(dice)}",width=15,height=8)
    dice_lb.place(x=120,y=20)
def exit():
    msg = messagebox.askyesno("Confirm", "Are you sure you want to exit ?")
    if (msg == True):
        window.destroy()
    else:
        pass
roll_btn = Button(window,text="Roll Dice !",command=roll,width=15,bg="black",fg="white").place(x=30,y=280)
exit_btn = Button(window,text="Exit",command=exit,width=15,bg="black",fg="white").place(x=250,y=280)
my_lb = Label(window,text="Developed By Akshit Agarwal",bg="skyblue", fg="black",font=("cambria",11,"italic")).place(x=100,y=375)
window.mainloop()