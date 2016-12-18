from Tkinter import *
from datetime import datetime

#init stuff
top = Tk()

#GUI stuff
text = Text(top)
clock = datetime.now()
text.insert(INSERT, clock)		#inserts text at location
text.pack(fill = BOTH)		#geometry organizer
#loops main?
top.mainloop()
top.update_idletasks()

