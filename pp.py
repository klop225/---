from tkinter import *
count = 0
def clicked():
    global count
    count += 1
    lbl.config(text=f"{count}")

window = Tk()
window.title("HELLO")
window.geometry('400x250')
lbl = Label(window,text="тыкай")
lbl.grid(column=0,row=0)
btn = Button(window, text="НЕ НАЖИМАЙ", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()