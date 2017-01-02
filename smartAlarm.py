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
		self.labelPage = Label(text = "Clock")
		self.labelClock = Label(text = "", font = self.clockFont)	#create object
		self.labelLeft = Label(text = "left")
		self.labelRight = Label(text = "right")
		self.root.bind("=", self.OnInc)	#attempted to keybind but having error
		self.root.bind("-", self.OnDec)
		self.bInc = Button(text = "+", command = self.OnInc)
		self.bDec = Button(text = "-", command = self.OnDec)

		width = self.root.winfo_width()
		height = self.root.winfo_height()

	#"organize" label wrt window using grid geometry
		self.labelPage.grid(row = 0, column = 0)
		self.labelClock.grid(row = 1, column = 0, columnspan = 4)
		self.labelLeft.grid(row = 2, column = 0)	
		self.labelRight.grid(row = 2, column = 3)
		self.bInc.grid(row = 2, column = 1)
		self.bDec.grid(row = 2, column = 2)

		self.root.columnconfigure(1, weight = 1)
		self.root.rowconfigure(1, weight = 1)

		#clock() is a meth that continuously fetches time and updates label
		self.clock()					#call clock method
		#self.fontInit()
		self.fontUpdate()
		
		self.root.mainloop()			#call 'mainloop' from root object to listen for events

	def clock(self):
		clockData = datetime.now()	#fetch current time
		#clockData = datetime.strptime("Sun", "%a")	#fetch current time

	#Label way of updating time
		self.labelClock.configure(text = clockData)	#raw time information
		self.labelClock.configure(text = datetime.strftime(clockData, "%H:%M:%S\n%a, %b %d"))

		self.root.after(1000, self.clock)	#have self.root call itself after 1000ms

	def fontInit(self):
		width = self.root.winfo_width()
		height = self.root.winfo_height()
		newSizeW = int(0.333 * height - 26.667)
		self.clockFont.configure(size = newSizeW)

		#self.root.after(200, self.fontUpdate((width, height)))	#have self.root call itself after 1000ms

	def fontUpdate(self):	#add in additional params to chart history (to determine when to stop)
		width = self.root.winfo_width()
		widthR = self.root.winfo_reqwidth()
		height = self.root.winfo_height()
		heightR = self.root.winfo_reqheight()
		if width < widthR or height < heightR:
			self.OnDec()
		elif width > widthR or height > heightR:
			self.OnInc()
		self.testMeas(self.clockFont['size'])
		if 1:	#use this if condition to stop call after history indicates it should stop
			self.root.after(10, self.fontUpdate)	#have self.root call itself after 1000ms
	
	def OnInc(self):
		size = self.clockFont['size']
		self.clockFont.configure(size = size + 1)
		self.testMeas(size)

	def OnDec(self):
		size = self.clockFont['size']
		if size - 2 > 0:
			self.clockFont.configure(size = size - 1)
		else:
			print "smallest possible size!"
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
