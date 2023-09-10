import tkinter as tk
import math
import random
import time

class App:
    def __init__(self, master):
        self.R = 300/math.sqrt(3)
        rad = 4.71239
        self.a = (300+self.R*math.cos(rad),300+self.R*math.sin(rad))
        self.b = (300+self.R*math.cos(rad+(2*math.pi)/3),300+self.R*math.sin(rad+(2*math.pi)/3))
        self.c = (300+self.R*math.cos(rad+(4*math.pi)/3),300+self.R*math.sin(rad+(4*math.pi)/3))
        self.steps = 0
        self.current_coord = (0,0)
        self.master = master
        self.canvas = tk.Canvas(master, width=600, height=600, borderwidth=2, relief='solid')
        self.canvas.create_oval(self.a[0]-4,self.a[1]-4,self.a[0]+4,self.a[1]+4, fill="red")
        self.canvas.create_oval(self.b[0]-4,self.b[1]-4,self.b[0]+4,self.b[1]+4, fill="red")
        self.canvas.create_oval(self.c[0]-4,self.c[1]-4,self.c[0]+4,self.c[1]+4, fill="red")
        self.canvas.pack()
        self.x1_button = tk.Button(master, text="x1", command=self.x1)
        self.x1_button.pack(side='left')
        self.x10_button = tk.Button(master, text="x10", command=self.x10)
        self.x10_button.pack(side='right')
        self.x100_button = tk.Button(master, text="x100", command=self.x100)
        self.x100_button.pack(side='right')
        self.x1000_button = tk.Button(master, text="x1000", command=self.x1000)
        self.x1000_button.pack(side='right')

    def draw_circle(self,coords,color,size):
        self.canvas.create_oval(coords[0]-size,coords[1]-size,coords[0]+size,coords[1]+size,fill=color,outline=color)

    def half_point(self,current_coord,root):
        x = (current_coord[0]+root[0])/2
        y = (current_coord[1]+root[1])/2
        return (x,y)

    def x1(self):
        if self.steps==0:
            self.current_coord = self.half_point(self.a,self.b)
            self.draw_circle(self.current_coord,"green",2)
            self.steps+=1
        else:
            self.draw_circle(self.current_coord,"white",2)
            self.draw_circle(self.current_coord,"red",1)
            self.current_coord=self.half_point(self.current_coord,random.choice([self.a,self.b,self.c]))
            self.draw_circle(self.current_coord,"green",2)
        print("x1 button pressed")

    def x10(self):
        for i in range(10):
            self.x1()
            #time.sleep(0.001)
            #self.canvas.update_idletasks()

    def x100(self):
        for i in range(10):
            self.x10()

    def x1000(self):
        for i in range(100):
            self.x10()        
            

root = tk.Tk()
app = App(root)
root.mainloop()