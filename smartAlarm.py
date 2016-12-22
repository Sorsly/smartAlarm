from Tkinter import *
from datetime import datetime

class TimeApp():
	def __init__(self):
		self.root = Tk()	#init stuff
		self.label = Label(text = "")
		self.label.pack()
		self.clock()
		self.root.mainloop()	#loops main

	def clock(self):
		clockData = datetime.now()	#fetch current time
		self.label.configure(text = clockData)
		#text = Text(self.root)	#text widget that allows text to be placed into window
		#text.insert(INSERT, clock)		#inserts current time at current location in text
		#text.pack(fill = BOTH)		#geometry organizer
		self.root.after(1000, self.clock)	#have self.root call itself after 1000ms

timeApp = TimeApp()
