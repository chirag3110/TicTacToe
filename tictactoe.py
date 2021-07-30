from tkinter import *
from PIL import Image,ImageTk
from functools import partial
import random
from tkinter import messagebox
from copy import deepcopy

sign=0
button=[]

global board
board = [[" " for x in range(3)] for y in range(3)]

root=Tk()
root.title("TIC-TAC-TOE")
root.geometry("400x400")

bg=Image.open("bg.jpg")
bg=bg.resize((900,1000))
bg=ImageTk.PhotoImage(bg)
canvas1=Canvas(height=400,width=400)
canvas1.pack()
canvas1.create_image(0,0,image=bg)

img=Image.open("ttt.png")
img=img.resize((400,200))
img=ImageTk.PhotoImage(img)
canvas1.create_image(200,80,image=img)

def winner(b, l):
    if (b[0][0] == l and b[0][1] == l and b[0][2] == l):
        return True
    elif (b[1][0] == l and b[1][1] == l and b[1][2] == l):
        return True
    elif (b[2][0] == l and b[2][1] == l and b[2][2] == l):
        return True
    elif (b[0][0] == l and b[1][0] == l and b[2][0] == l):
        return True
    elif (b[0][1] == l and b[1][1] == l and b[2][1] == l):
        return True
    elif (b[0][2] == l and b[1][2] == l and b[2][2] == l):
        return True
    elif (b[0][0] == l and b[1][1] == l and b[2][2] == l):
        return True
    elif (b[0][2] == l and b[1][1] == l and b[2][0] == l):
        return True


def isfull():
    flag = True
    for i in board:
        if(i.count(' ') > 0):
            flag = False
    return flag


def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner)-1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge)-1)
            return edge[move]


def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            board[i][j] = "X"
            button[i][j].config(text=board[i][j],bg="#003F87",fg="white")
        else:
            board[i][j] = "O"
            button[i][j].config(text=board[i][j],bg="#B22222",fg="white")    

        sign += 1
    else:
        messagebox.showerror("OOPS","Invalid Move")
    x = True
    if winner(board, "X"):
        x = False
        messagebox.showinfo("Winner", "Player won the match")
        root.destroy()
    elif winner(board, "O"):
        x = False
        messagebox.showinfo("Winner", "Computer won the match")
        root.destroy()
    elif isfull():
        x = False
        messagebox.showinfo("Tie Game", "Tie Game")
        root.destroy()
    if(x):
        if sign % 2 != 0:
            
            move = pc()
            get_text_pc(move[0], move[1], gb, l1, l2)

    
def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        button.append(i)
        button[i] = []
        for j in range(3):
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(game_board,command=get_t, height=4, width=8,font=("bold"))
            button[i][j].grid(row=i, column=j)


def get_text(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=NORMAL,borderwidth=2,relief="groove",bg="#B22222",fg="white")
            board[i][j] = "X"
            button[i][j].config(text=board[i][j],bg="#003F87",fg="white")
        else:
            l2.config(state=DISABLED)
            l1.config(state=NORMAL,bg="#003F87",fg="white",borderwidth=2,relief="groove")
            board[i][j] = "O"
            button[i][j].config(text=board[i][j],bg="#B22222",fg="white")
        sign += 1
        
    if winner(board, "X"):
        messagebox.showinfo("Winner", "Player 1 won the match")
        root.destroy()
    elif winner(board, "O"):
        messagebox.showinfo("Winner", "Player 2 won the match")
        root.destroy()
    elif(isfull()):
        messagebox.showinfo("Tie Game", "Tie Game")
        root.destroy()


def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        button.append(i)
        button[i] = []
        for j in range(3):
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(game_board,command=get_t, height=4, width=8,font=("bold"))
            button[i][j].grid(row=i, column=j)


def wpl():
    global root
    for widget in root.winfo_children():
        widget.destroy() 
    root.config(bg="light blue")
    player_frame=Frame(bg="light blue")
    player_frame.pack(pady=20)
    l1 = Button(player_frame,text="Player 1 : X",font=("Helvetica",12), width=10,bg="#003F87",fg="white",borderwidth=2,relief="groove")
    l1.pack(side=LEFT,padx=10,ipadx=10)
    l2 = Button(player_frame,text = "Player 2 : O",font=("Helvetica",12),width = 10, state = DISABLED,borderwidth=2,relief="groove",bg="#B22222",fg="white")
    l2.pack(side=RIGHT,padx=10,ipadx=10)
    board=Frame()
    board.pack(pady=15)
    gameboard_pl(board, l1, l2)


def wpc():
    global root
    for widget in root.winfo_children():
        widget.destroy() 
    root.config(bg="light blue")
    player_frame=Frame(bg="light blue")
    player_frame.pack(pady=20)
    l1 = Label(player_frame,text="Player : X",font=("Helvetica",12), width=10,bg="#003F87",fg="white",borderwidth=2,relief="groove")
    l1.pack(side=LEFT,padx=10,ipadx=10,ipady=3)
    l2 = Label(player_frame,text = "Computer : O",font=("Helvetica",12),width = 10,borderwidth=2,relief="groove",bg="#B22222",fg="white")
    l2.pack(side=RIGHT,padx=10,ipadx=10,ipady=3)
    board=Frame()
    board.pack(pady=15)
    gameboard_pc(board, l1, l2)


btn_wpc=Button(text="Single Player",font=("Helvetica",15),command=wpc,width=15,bg="#162252",fg="white")
btn_wpl=Button(text="Multiplayer",font=("Helvetica",15),command=wpl,width=15,bg="#162252",fg="white")
btn_exit=Button(text="Exit",font=("Helvetica",15),width=15,command=root.destroy,bg="#162252",fg="white")

btn_canvas1=canvas1.create_window(200,200,window=btn_wpc)
btn_canvas2=canvas1.create_window(200,250,window=btn_wpl)
btn_canvas3=canvas1.create_window(200,300,window=btn_exit)

root.mainloop()