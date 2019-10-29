from tkinter import *
from tkinter import messagebox
import time
from random import *

mw = Tk()
mw.title("Classic SNAKE")
score = -1
ht,wt = 300,300
snkx,snky = ht/20, wt/20
label = Label(mw,text = f"SCORE : {score}",font =("times",15,"bold"), bg = "white")
c = Canvas(mw, bg = "white", cursor = "plus", height = ht, width = wt)
label.pack(expand = 1, fill=BOTH)
c.pack(expand=0)

#initial coords
x1, y1 = 0, 0
x2, y2 = snkx, snky
p, q = 0, 0
after = c.after(10000,lambda : 0)

#create snake head
head = c.create_rectangle(x1,y1,x2,y2,fill="#6a5acd", outline="black", width = "2")
bodylen = 1
tails = []
tail_id = [None]

#create food
fud = c.create_oval(0,0,snkx,snky)

def check_death():
    global after,ht
    a,b,d,e = c.coords(head)
    if(c.coords(head) in tails or a < 0 or b < 0 or e > ht or d > wt):
        label.config(text = "GAME OVER :(")
        c.after_cancel(after)
        if messagebox.showinfo("Result", "CHI CHI YOU LOST"):
            exit()


def update_tail(callfrmgrow = 0):
    global tails,tail_id
    tails.append(c.coords(head))
    tails = tails[-(bodylen):]
    tail_id.append(c.create_rectangle(c.coords(head), fill="#6a5acd", outline="black", width="2"))
    if callfrmgrow == 0 :
        temp = tail_id.pop(0)
        c.delete(temp)


def move(a,b):
    global x1,y1,x2,y2,head,after,tails,body,bodylen,first
    c.move(head, a*snkx,b*snky)
    check_death()

    x1, y1 = x1+(snkx*a),y1+(snky*b)
    x2, y2 = x2+(snkx*a),y2+(snky*b)
    if(x1 == p and y1 == q):
        food()
        grow()
    elif any(tails):
        update_tail()

    if(a==1):
        c.after_cancel(after)
        after = c.after(180,lambda :right(0))
    if(a==-1):
        c.after_cancel(after)
        after = c.after(180, lambda: left(0))
    if(b==-1):
        c.after_cancel(after)
        after = c.after(180, lambda: up(0))
    if(b==1):
        c.after_cancel(after)
        after = c.after(180, lambda: down(0))


def grow():
    global bodylen,tails
    update_tail(1)
    bodylen+=1


def food():
    global p,q,fud, score,tails
    score += 1
    label.config(text = f"SCORE : {score}")
    p=snkx*randrange(1,snkx)
    q=snky*randrange(1,snky)
    c.delete(fud)
    fud = c.create_oval(p,q,p+snkx,q+snky, fill = "red", outline = "black", width = " 3")


def left(event):
    #print("left")
    move(-1,0)

def right(event):
    #print("right")
    move(1, 0)

def up(event):
    #print("up")
    move(0, -1)

def down(event):
    #print("down")
    move(0, 1)

mw.bind("<Right>",right)
mw.bind("<Left>",left)
mw.bind("<Up>", up)
mw.bind("<Down>", down)
food()

mainloop()
