from tkinter import *
import vlc

p = vlc.MediaPlayer("gol.mp3")
p.play()

p.stop()

tk=Tk()
tk.title("Prueba1")
canvas=Canvas(tk,width=500, height=228)
canvas.pack()
my_image=PhotoImage(file="Dfondo.gif")
canvas.create_image(0,0,anchor=NW,image=my_image)
my_image2=PhotoImage(file="arco.gif")
canvas.create_image(0,0,anchor=NW,image=my_image2)
my_image4 = PhotoImage(file="pelota3.gif")
canvas.create_image(300, 100, anchor=NW, image=my_image4)

def movetriangle(event):
    canvas.move(3, 5, 0)


def movetriangle1(event):
    canvas.move(3, -5, 0)
    #canvas.move(4,-5,0)

def movetriangle2(event):
    canvas.move(3, 0, -5)

def movetriangle3(event):
    canvas.move(3, 0, 5)
pos = canvas.coords(3)
canvas.bind_all("<KeyPress-Up>", movetriangle2)
canvas.bind_all("<KeyPress-Down>", movetriangle3)
canvas.bind_all("<KeyPress-Right>", movetriangle)
canvas.bind_all("<KeyPress-Left>", movetriangle1)

tk.mainloop()
print(pos)
print("goool")