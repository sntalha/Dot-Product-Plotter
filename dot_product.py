from tkinter import *
from tkinter import Button as But
import matplotlib.pyplot as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def dot_product():
    global result
    v1=[]
    v2=[]
    v1.append(e1.get())
    v1.append(e2.get())
    v1.append(e3.get())
    v2.append(e4.get())
    v2.append(e5.get())
    v2.append(e6.get())
    result = 0
    for i in range(len(v1)):
        prod = int(v1[i]) * int(v2[i])
        result += prod

    dpframe = Frame(frame2, bg="Red")
    dp = Label(dpframe, text="Dot Product", bg="Red", font=("Ariel", 15))
    ans= Label(dpframe, text=result,bg="white",width=5,font=("Ariel", 15))
    dpframe.pack(pady=50, padx=50)
    dp.pack()
    ans.pack()
    fig = mpl.figure()

    ax= fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], arrow_length_ratio=0.1,
               length=(result*0.9), normalize=True, color='r')
    ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], normalize=True, color='green',
               length=(result*0.9), arrow_length_ratio=0.1)

    # Add a dot at the location of the dot product on the x-axis
    ax.plot([result], [0], [0], marker='.', markersize=10, color='blue')

    ax.set_xlim([-10-result, result+10])
    ax.set_ylim([-10-result, result+10])
    ax.set_zlim([-10-result, result+10])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    canvas = FigureCanvasTkAgg(fig, master=frame1)
    canvas.get_tk_widget().pack()

    canvas.draw()
m=Tk()
m.title("Applied Physics Assignment")

heading=Label(m,text="Dot Product",font=("Times New Romain",25),bg="Black",fg="Grey",height=2,width=32)
heading.pack(side=TOP)

frame1=Frame(m,height=400,width=300,bg="white")
frame1.pack(side=LEFT)
frame2=Frame(m,height=400,width=300,bg="black")
frame2.pack(side=RIGHT)

v1frame=Frame(frame2,bg="black")
vector1=Label(v1frame,text="Enter First Vector",bg="pink",font=("Ariel",15))
e1=Entry(v1frame,font=("Ariel",15),width=3)
i1=Label(v1frame,text="i + ",bg="cyan",font=("Ariel",15))
e2=Entry(v1frame,font=("Ariel",15),width=3)
j1=Label(v1frame,text="j +",bg="cyan",font=("Ariel",15))
e3=Entry(v1frame,font =("Ariel",15), width=3)
z1= Label(v1frame,text="z",bg="cyan",font=("Ariel",15))
vector1.grid(row=0,column=0,columnspan=5)
e1.grid(row=1,column=0)
i1.grid(row=1,column=1)
e2.grid(row=1,column=2)
j1.grid(row=1,column=3)
e3.grid(row=1,column=4)
z1.grid(row=1,column=5)
v1frame.pack(pady=50,padx=50)
v2frame=Frame(frame2,bg="black")
vector2=Label(v2frame,text="Enter Second Vector",bg="pink",font=("Ariel",15))
e4=Entry(v2frame,font=("Ariel",15),width=3)
i2=Label(v2frame,text="i + ",bg="cyan",font=("Ariel",15))
e5=Entry(v2frame,font=("Ariel",15),width=3)
j2=Label(v2frame,text="j +",bg="cyan",font=("Ariel",15))
e6=Entry(v2frame,font=("Ariel",15),width=3)
z2=Label(v2frame,text="z",bg="cyan",font=("Ariel",15))
vector2.grid(row=0,column=0,columnspan=5)
e4.grid(row=1,column=0)
i2.grid(row=1,column=1)
e5.grid(row=1,column=2)
j2.grid(row=1,column=3)
e6.grid(row=1,column=4)
z2.grid(row=1,column=5)
v2frame.pack(pady=50,padx=50)

plt=But(frame2,text="Plot",height=2,bg="Grey",fg="black",command=dot_product)
plt.pack()


m.mainloop()
