from tkinter import *

root = Tk()

disp = Entry(root)
disp.grid(row=0, columnspan=4, sticky=EW)

but_lst = ['Cls', 'Back', '', 'Close', '7','8','9','/','4','5','6','8','1','2','3','-','0','.','=','+']

i=int(0)
for item in but_lst:
    but = Button(root, text=item, width=10)
    but.grid(row=i//4+1, column=i%4)
    i += 1

root.mainloop()
