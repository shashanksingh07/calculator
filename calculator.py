from tkinter import*

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
               
            except Exception as e:
                print(e)
                value="ERROR"
            scvalue.set(value)
            screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

def special(event):
        global  scvalue
        scvalue.set("Hello Sir!")
        screen.update()

root = Tk()
root.geometry("300x500")
root.title("calculator")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue, font="lucida 18 bold")
screen.pack(fill=X,padx=8,pady=8,ipadx=20,ipady=10)




f=Frame(root,bg="grey")

b=Button(f,text="9",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=1,column=1)

b=Button(f,text="8",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=1,column=2)

b=Button(f,text="7",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=1,column=3)

b=Button(f,text="+",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=1,column=4)

f.pack()



f=Frame(root,bg="grey")

b=Button(f,text="6",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=2,column=1)

b=Button(f,text="5",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=2,column=2)
b=Button(f,text="4",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=2,column=3)
b=Button(f,text="-",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=2,column=4,ipadx=4)
f.pack()


f=Frame(root,bg="grey")

b=Button(f,text="3",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=3,column=1)

b=Button(f,text="2",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=3,column=2)

b=Button(f,text="1",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=3,column=3)

b=Button(f,text="/",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=3,column=4,ipadx=4)



f.pack()


f=Frame(root,bg="grey")

b=Button(f,text="=",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=5,column=1)

b=Button(f,text="0",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=5,column=2)

b=Button(f,text=".",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=5,column=3,ipadx=3)
b=Button(f,text="*",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=5,column=4,ipadx=3)

f.pack()



f=Frame(root,bg="grey")

b=Button(f,text="C",padx=10,pady=10,font="lucida 20 bold",relief=SUNKEN)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b.grid(row=6,column=1,ipadx=5)

# b=Button(f,text="00",padx=10,pady=10,font="lucida 18 bold",relief=SUNKEN)
# # b.pack(side=LEFT,padx=10,pady=10)
# b.bind("<Button-1>",click)
# b.grid(row=6,column=2,ipadx=2)

b=Button(f,text="Special",padx=10,pady=10,font="lucida 23 bold",relief=SUNKEN,borderwidth=2)
# b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",special)
b.grid(row=6,column=2,ipadx=4)


f.pack()



root.mainloop()

