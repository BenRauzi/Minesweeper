from tkinter import *
from tkinter import ttk
import random

def init():
	global var, label, root

	root= Tk()
	root.title("Minesweeper")
	root.geometry("250x65+500+100")
	root.resizable(0,0)

	label = Label(root, text="Enter the grid size:")
	label.pack()

	var = StringVar()
	entry = ttk.Entry(root, textvariable=var, width=40)
	entry.pack()

	enterButton = ttk.Button(root, width=50, text="Start", command=tryStart)
	enterButton.pack()

	root.mainloop()

def tryStart():
	global cols
	try:
		cols = int(var.get())
		if (cols < 100):
			root.destroy()		
			start(cols)
		else:
			print("Not a valid input")
			label["text"] = "Please Enter a Valid Input"
			var.set("")
	except ValueError:
		print("Not a valid input")
		label["text"] = "Please Enter a Valid Input"
		var.set("")


def start(cols):
	global mainRoot, arr, bombs, revealedButtons, flagPositions
	mainRoot = Tk()
	mainRoot.title("Minesweeper")


	master = LabelFrame(mainRoot, text="Minesweeper")
	master.pack()

	frameTop = Frame(master)
	frameTop.pack()

	topButton = ttk.Button(frameTop, text="Restart", width=int(5.5*cols), command=restart)
	topButton.pack()

	frameMain = Frame(master)
	frameMain.pack()

	flagPositions = []
	arr = []
	bombs = []
	for x in range(cols):
		for y in range(cols):
			arr.append(ttk.Button(frameMain,width=4, text="{}, {}".format(x,y), command=lambda x=x, y=y: onClick(x,y)))
			arr[-1].bind("<Button-3>", lambda z=1, x=x, y=y: onRightClick(z,x,y))
			arr[-1].grid(row=x, column=y)


			if random.randint(0,cols) < cols/5:
				if 	x == 0 or y == 0 or x*y in bombs:
					continue
				bombs.append(x*y)
	bombs.sort()
	print(bombs)


	revealedButtons = []
	mainRoot.resizable(0,0)
	mainRoot.mainloop()

def onClick(x,y):
	print("Debug --", x,y, y + x * cols)

	position = y + x * cols
	if position in bombs:
		end(False)
		arr[position]["text"] = "Bomb"
	else:
		reveal(position, x, y)
def onRightClick(this,x,y):
	position = y + x * cols

	print(x,y, position)

	if not position in flagPositions:
		flagPositions.append(position)
		arr[position]["text"] = "Flag"
	else:
		flagPositions.remove(position)
		arr[position]["text"] = "{}, {}".format(x,y)

	print(flagPositions)
	print(bombs)
	flagPositions.sort()
	if flagPositions == bombs:
		print("Win")
		end(True)

def reveal(args ,x ,y):

	if args in revealedButtons:
		return 0;
	revealedButtons.append(args)

	if x==0:
		params=[args-cols,args-cols+1,args+1,args+cols,args+cols+1]
	elif x==9:
		params=[args-cols-1,args-cols,args-1,args+cols-1,args+cols]
	else:
		params= [args-cols-1,args-cols,args-cols+1,args-1,args+1,args+cols-1,args+cols,args+cols+1]
	
	nearBombs=0
	for i in params:
		if i in bombs and i > 0 and i < cols**2:
			nearBombs+=1

	arr[args]["text"] = nearBombs

	if nearBombs == 0:
		for i in [args-cols,args-1,args+1,args+cols]:
			try:
				if i < 10 and i > 0:
					reveal(i, 0, str(i))
				if i < 100 and i > 0 and i < cols**2:
					reveal(i, str(i)[0], str(i)[1])
				elif i > 0 and i < cols**2:
					reveal(i, str(i)[0:2], str(i)[2])
			except IndexError:
				pass

def end(cond):
	print("Game Over")
	for i in arr:

		i["state"] = "disabled"

def restart():
	mainRoot.destroy()
	init()

def scoreBoard():
	scoreBoard = Tk()
	scoreBoard.title("High Scores")
	scoreBoard.resizable(0,0)

	title = ttk.Label(scoreBoard, text="High Scores")
	title.pack(pady=5)

	frameMain = Frame(scoreBoard)
	frameMain.pack()

	highScoreList = Listbox(scoreBoard, width=50)
	highScoreList.pack()

	highScoreList.insert(END,"Test")

	highScoreList.insert(END,"Test2")

	scoreBoard.mainloop()

def addScore():
	pass
init()
#scoreBoard()

