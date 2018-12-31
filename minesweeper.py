import tkinter as tk
import random

def restart():
	root.destroy()
	start()

def start():
	global root, col, bombCount, bombPositions, button,flagged
	col = 10
	bombCount = 20
	bombPositions=[]
	button = list()
	flagged=[]
	root = tk.Tk()
	root.title("Minesweeper")
	root.resizable(0, 0)
	del bombPositions[:]
	frame = tk.Frame(root)
	frame.pack()

	new = tk.Button(frame, text="RESTART", fg="red",width=53, height=1,command=restart)
	new.pack(side=tk.LEFT)

	frame1 = tk.Frame(root)
	frame1.pack(side=tk.TOP, fill=tk.X)
	buttonCount = []
	for y in range(col):
		for x in range(col):
			button.append(tk.Button(frame1,width=4,height=2, command=lambda x=x, y=y: onClick(x, y)))
			button[-1].bind('<Button-3>', lambda z=1, x=x, y=y: onRightClick(x,y)) #z=1 for some reason requited, or lambda function argument recieves binding stuff
			button[-1].grid(row=y,column=x)
			buttonCount.append((y*10)+x)
	createBombs()


	root.mainloop()

def onRightClick(x,y):

	i = (10*y)+x

	if not ((button[i])["text"]) == "Flag":
		(button[i])["text"] = "Flag"
		(button[i])["state"]="disabled"
		flagged.append(i)
		flagged.sort()

		if flagged == bombPositions:
			end(1)

	else:
		(button[i])["state"]="active"
		(button[i])["text"] = ""
		flagged.remove(i)

def onClick(x, y):
	if not end == 1:
		i = (10*y)+x
		print("%sx %dy, position %s" % (x,y, i))

		if i in bombPositions:
			end(0)
			(button[i])["text"] = "Bomb"
		else:
			params1 = [i-col-1,i-col,i-col+1,i-1,i+1,i+col-1,i+col,i+col+1]
			params2 = [i-col,i-col+1,i+1,i+col,i+col+1]
			params3 = [i-col-1,i-col,i-1,i+col-1,i+col]
			
			if not(x==0 or x==9):
				params=params1
			elif x==0:
				params=params2
			elif x==9:
				params=params3

			bombs=0
			for u in params:
				if u in bombPositions:
					bombs+=1

			(button[i])["text"] = bombs


def createBombs():
	for x in range(bombCount):
		bombPositions.append(random.randint(0,col**2))

	bombPositions.sort()
def end(win):
	for y in range(col):
		for x in range(col):
			i = (10*y)+x
			(button[i])["state"]="disabled"
			if i in bombPositions:
				(button[i])["text"] = "Bomb"
			else:
				params1 = [i-col-1,i-col,i-col+1,i-1,i+1,i+col-1,i+col,i+col+1]
				params2 = [i-col,i-col+1,i+1,i+col,i+col+1]
				params3 = [i-col-1,i-col,i-1,i+col-1,i+col]
				
				if not(x==0 or x==9):
					params=params1 
				elif x==0:
					params=params2
				elif x==9:
					params=params3

				bombs=0
				for u in params:
					if u in bombPositions:
						bombs+=1

				(button[i])["text"] = bombs

	if win == 1:
		print("Win")
	else:
		print("Loss")

start()