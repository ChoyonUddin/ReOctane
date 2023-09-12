from tkinter import *

'''
root = Tk(className="test")
environment = Entry(root,bg='White',fg='Blue',border=5,borderwidth=5,)
environment.pack()



def on_click():
    my_label = Label(root,text=environment.get())#.grid(column=1,row=1)
    my_label.pack()
   

#Button This will become a slider later maybe with some button implementation
my_button = Button(root,text="Calculate",command=on_click)
my_button.pack()



root.mainloop()
'''

my_slider = Scale(Tk(className="Test"),orient=HORIZONTAL,borderwidth=5,border=5,from_=0, to=250*1000,)
my_slider.pack()

mainloop()
