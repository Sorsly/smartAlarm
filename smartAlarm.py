from Tkinter import *
from datetime import datetime
import tkFont

class TimeApp():
	def __init__(self):

		#Tk() is top level object containing everything else
		self.root = Tk()				#create object 
		self.clockFont = tkFont.Font(family = "Calibri", size = 12)

	#choose Label or Text way of showing time
	#Label() is a widget under Tk()
		self.labelLeft = Label(text = "left")
		self.labelRight = Label(text = "right")
		self.labelClock = Label(text = "", font = self.clockFont)	#create object
		self.bInc = Button(text = "+", command = self.OnInc)
		self.bDec = Button(text = "-", command = self.OnDec)

	#"organize" label wrt window using grid geometry
		self.labelLeft.grid(row = 0, column = 0)	
		self.labelClock.grid(row = 1, column = 1)
		self.labelRight.grid(row = 0, column = 2)
		self.bInc.grid(row = 2, column = 2)
		self.bDec.grid(row = 3, column = 2)

		self.root.columnconfigure(1, weight = 1)
		self.root.rowconfigure(1, weight = 1)

	#Text() way of showing time
		#self.text = Text(self.root)	#also valid, but specification of window unnecessary here
		#self.text = Text()		#text widget that allows text to be placed into window
		#self.text.pack()

		#clock() is a meth that continuously fetches time and updates label
		self.clock()					#call clock method
		
		self.root.mainloop()			#call 'mainloop' from root object to listen for events

	def clock(self):
		clockData = datetime.now()	#fetch current time
		#clockData = datetime.strptime("Sun", "%a")	#fetch current time

	#choose Label or Text way of updating time
	#Label way of updating time
		#self.labelClock.configure(text = clockData)	#raw time information
		self.labelClock.configure(text = datetime.strftime(clockData, "%H:%M:%S\n%a, %b %d"))

	#Text way of updating time
		#self.text.delete(("0.0"),END)		#inserts current time at current location in text
		#self.text.insert(INSERT, clockData)		#inserts current time at INSERT index

		self.root.after(1000, self.clock)	#have self.root call itself after 1000ms

	def fontUpdate(self):
		self.labelClock.configure(size = newSize)
		self.root.after(2000, self.test)	#have self.root call itself after 1000ms
	
	def OnInc(self):
		width = self.labelClock['width']
		height = self.labelClock['height']
		size = self.clockFont['size']
		print(width)
		print(height)
		print(size)
		self.clockFont.configure(size = size + 2)

	def OnDec(self):
		size = self.clockFont['size']
		self.clockFont.configure(size = size - 2)
timeApp = TimeApp()
