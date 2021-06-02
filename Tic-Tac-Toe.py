from tkinter import *
from tkinter import messagebox
import win32gui , win32con

root = Tk()
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide,win32con.SW_HIDE)
root.geometry("321x500")
root.maxsize(321,500)
root.minsize(321,500)
root.title("Tic-Tac-Toe Game")
root.iconbitmap("C:\\Users\\prince\\Desktop\\GUI\\Required files\\Rock.ico")

score1 = 0  
score2 = 0  

# X starts so True
clicked = True
count = 0

def reset():
    b1["state"]=ACTIVE
    b2["state"]=ACTIVE
    b3["state"]=ACTIVE
    b4["state"]=ACTIVE
    b5["state"]=ACTIVE
    b6["state"]=ACTIVE
    b7["state"]=ACTIVE
    b8["state"]=ACTIVE
    b9["state"]=ACTIVE

    b1.config(text=" ",bg="papaya whip")
    b2.config(text=" ",bg="papaya whip")
    b3.config(text=" ",bg="papaya whip")
    b4.config(text=" ",bg="papaya whip")
    b5.config(text=" ",bg="papaya whip")
    b6.config(text=" ",bg="papaya whip")
    b7.config(text=" ",bg="papaya whip")
    b8.config(text=" ",bg="papaya whip")
    b9.config(text=" ",bg="papaya whip")

def dis_btn():
    b1["state"]=DISABLED
    b2["state"]=DISABLED
    b3["state"]=DISABLED
    b4["state"]=DISABLED
    b5["state"]=DISABLED
    b6["state"]=DISABLED
    b7["state"]=DISABLED
    b8["state"]=DISABLED
    b9["state"]=DISABLED

def check_result():
    global winner
    winner = False

    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        global score1,score2
        score1 +=1
        p1_score.config(text=score1)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X!! has won the game")
        dis_btn()

    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        score1 +=1
        p1_score.config(text=score1)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X!! has won the game")
        dis_btn()

    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        score1 +=1
        p1_score.config(text=score1)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X!! has won the game")
        dis_btn()

    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        score1 +=1
        p1_score.config(text=score1)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X!! has won the game")
        dis_btn()

    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        score1 +=1
        p1_score.config(text=score1)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X!! has won the game")
        dis_btn()

    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        score1 +=1
        p1_score.config(text=score1)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X!! has won the game")
        dis_btn()

    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        score1 +=1
        p1_score.config(text=score1)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X!! has won the game")
        dis_btn()

    elif b1["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        score1 +=1
        p1_score.config(text=score1)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X!! has won the game")
        dis_btn()

    # check for O wins

    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        score2 +=1
        p2_score.config(text=score2)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O!! has won the game")
        dis_btn()

    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        score2 +=1
        p2_score.config(text=score2)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O!! has won the game")
        dis_btn()

    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        score2 +=1
        p2_score.config(text=score2)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O!! has won the game")
        dis_btn()

    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        score2 +=1
        p2_score.config(text=score2)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O!! has won the game")
        dis_btn()

    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        score2 +=1
        p2_score.config(text=score2)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O!! has won the game")
        dis_btn()

    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        score2 +=1
        p2_score.config(text=score2)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O!! has won the game")
        dis_btn()

    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        score2 +=1
        p2_score.config(text=score2)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O!! has won the game")
        dis_btn()

    elif b1["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        score2 +=1
        p2_score.config(text=score2)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O!! has won the game")
        dis_btn()


def b_click(b):
    global clicked
    global count

    if b["text"]==" " and clicked==True:
        b["text"] = "X"
        b["fg"] = "lawn green"
        clicked = False
        count +=1
        check_result()

    elif b["text"]==" " and clicked==False:
        b["text"] = "O"
        b["fg"] = "deep sky blue"
        clicked = True
        count +=1
        check_result()

    else:
        messagebox.showerror("Tic-Tac-Toe","Hey! the box is already filled\n pick another box...")

b1 = Button(root,text=" ",font="lucida 20",height=3,width=6,bg="papaya whip",command = lambda:b_click(b1),relief=SUNKEN)
b2 = Button(root,text=" ",font="lucida 20",height=3,width=6,bg="papaya whip",command = lambda:b_click(b2),relief=SUNKEN)
b3 = Button(root,text=" ",font="lucida 20",height=3,width=6,bg="papaya whip",command = lambda:b_click(b3),relief=SUNKEN)

b4 = Button(root,text=" ",font="lucida 20",height=3,width=6,bg="papaya whip",command = lambda:b_click(b4),relief=SUNKEN)
b5 = Button(root,text=" ",font="lucida 20",height=3,width=6,bg="papaya whip",command = lambda:b_click(b5),relief=SUNKEN)
b6 = Button(root,text=" ",font="lucida 20",height=3,width=6,bg="papaya whip",command = lambda:b_click(b6),relief=SUNKEN)

b7 = Button(root,text=" ",font="lucida 20",height=3,width=6,bg="papaya whip",command = lambda:b_click(b7),relief=SUNKEN)
b8 = Button(root,text=" ",font="lucida 20",height=3,width=6,bg="papaya whip",command = lambda:b_click(b8),relief=SUNKEN)
b9 = Button(root,text=" ",font="lucida 20",height=3,width=6,bg="papaya whip",command = lambda:b_click(b9),relief=SUNKEN)

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

player1_score_lbl = Label(root,text = "Player 1 Score",font="lucida 13")
player1_score_lbl.place(x=10,y=370)

p1_score =  Label(root,text = "NIL",font="lucida 13",width=6,bg="white")
p1_score.place(x=20,y=400)

player2_score_lbl = Label(root,text = "Player 2 Score",font="lucida 13")
player2_score_lbl.place(x=200,y=370)

p2_score =  Label(root,text = "NIL",font="lucida 13",width=6,bg="white")
p2_score.place(x=210,y=400)

reset_btn = Button(root,text="Reset Game",font="lucida 10 bold",bg="red",fg="white",command=reset,relief=SUNKEN)
reset_btn.place(x=230,y=470)

root.mainloop()
