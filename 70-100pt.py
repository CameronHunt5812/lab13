#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class
enemie = drawpad.create_rectangle(100,300,200,340, fill="orange")
enemie2 = drawpad.create_rectangle(50,500,200,540, fill="blue")
enemie3 = drawpad.create_rectangle(500,50,560,90, fill="green")

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=1)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "green")
       	    self.right.grid(row=1,column=2)
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "green")
       	    self.left.grid(row=1,column=0)
       	    
       	    self.doun = Button(self.myContainer1)
       	    self.doun.configure(text="doun", background= "green")
       	    self.doun.grid(row=1,column=1)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    self.doun.bind("<Button-1>", self.dounClicked)
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    global enemie
	    global enemie2
	    global enemie3
	    x1, y1, x2, y2 = drawpad.coords(enemie)
	    x3, y3, x4, y4 = drawpad.coords(enemie2)
	    x5, y5, x6, y6 = drawpad.coords(enemie3)
	    drawpad.move(enemie,6,0)
	    drawpad.move(enemie2,-4,0)
	    drawpad.move(enemie3,8,0)
	    if x2 > drawpad.winfo_width():
                drawpad.move(enemie, -(drawpad.winfo_width()) + (x2 - x1),0)
            if x3 < 0:
                drawpad.move(enemie2, (drawpad.winfo_width()) - (x4 - x3),0)
            if x6 > drawpad.winfo_width():
                drawpad.move(enemie3, -(drawpad.winfo_width()) + (x6 - x5),0)
	    # Uncomment this when you're ready to test out your animation!
	    drawpad.after(10,self.animate)
		
	def upClicked(self, event):   
	    global oval
	    global player
	    drawpad.move(player,0,-10)
        def rightClicked(self, event):
            global oval
	    global player
	    drawpad.move(player,10,0)
        def leftClicked(self, event):
            global oval
	    global player
	    drawpad.move(player,-10,0)
	def dounClicked(self, event):
	    global oval
	    global player
	    drawpad.move(player,0,10)

app = MyApp(root)
root.mainloop()