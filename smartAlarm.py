from Tkinter import *
from datetime import datetime
import tkFont

class TimeApp():
	def __init__(self):

		#Tk() is top level object containing everything else
		self.root = Tk()				#create object 
		self.clockFont = tkFont.Font(family = "Andale Mono", size = 12)

	#choose Label or Text way of showing time
	#Label() is a widget under Tk()
		self.labelLeft = Label(text = "left")
		self.labelRight = Label(text = "right")
		self.labelClock = Label(text = "", font = self.clockFont)	#create object
		self.root.bind("=", self.OnInc)	#attempted to keybind but having error
		self.root.bind("-", self.OnDec)
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
		#self.fontUpdate()
		
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
		width = self.root.winfo_width()
		height = self.root.winfo_height()
		newSizeW = int(round(0.333 * height - 26.667, 0))
		newSizeH = 0
		#newSizeH not implemented yet (nonlinear, possibly due to font type)
		if newSizeW < newSizeH:
			newSize = newSizeW
		else:
			newSize = newSizeH
		self.clockFont.configure(size = newSize)
		self.root.after(2000, self.fontUpdate)	#have self.root call itself after 1000ms
	
	def OnInc(self):
		size = self.clockFont['size']
		self.clockFont.configure(size = size + 2)
		self.testMeas(size)

	def OnDec(self):
		size = self.clockFont['size']
		self.clockFont.configure(size = size - 2)
		self.testMeas(size)
	
	def testMeas(self, size):	#feel free to remove later; used to figure out window size
		width = self.labelClock.winfo_width()
		widthR = self.labelClock.winfo_reqwidth()
		widthWin = self.labelClock.winfo_width()
		height = self.labelClock.winfo_height()
		heightR = self.labelClock.winfo_reqheight()
		heightWin = self.root.winfo_height()
		print("width:", width)
		print("widthR:", widthR)
		#print('widthWin:', widthWin)
		print("height:", height)
		print("heightR:", heightR)
		#print('heightWin:', heightWin)
		print(size)

timeApp = TimeApp()
