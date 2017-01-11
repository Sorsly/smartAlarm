from Tkinter import *
from datetime import datetime
import tkFont

global bgCol 
global fgCol
bgCol = "black"
fgCol = "white"

class TimeApp():
	def __init__(self):

		#Tk() is top level object containing everything else
		self.root = Tk()				#create object 
		self.root.attributes('-zoomed', True) #maximizes window so visible
		self.clockFont = tkFont.Font(family = "Andale Mono", size = 12)

	#Label() is a widget under Tk()
		self.labelPage = Label(text = "Clock")
		self.labelClock = Label(text = "", font = self.clockFont)	#create object
		#self.labelLeft = Label(text = "left")
		#self.labelRight = Label(text = "right")
		#self.bInc = Button(text = "+", command = self.OnInc)
		#self.bDec = Button(text = "-", command = self.OnDec)

	#"organize" label wrt window using grid geometry
		self.labelPage.grid(row = 0, column = 0)
		self.labelClock.grid(row = 1, column = 0, columnspan = 4)
		#self.labelLeft.grid(row = 2, column = 0)	
		#self.labelRight.grid(row = 2, column = 3)
		#self.bInc.grid(row = 2, column = 1)
		#self.bDec.grid(row = 2, column = 2)

		self.root.columnconfigure(1, weight = 1)	#centers wrt grid system
		self.root.rowconfigure(1, weight = 1)		#centers wrt grid system

		self.state = False	#inits fullscreen state
	#bindings
		#bindings can call functions defined with these params (self, event=None)
		self.root.bind("=", self.OnInc)	#attempted to keybind but having error
		self.root.bind("-", self.OnDec)
		self.root.bind("<F11>", self.toggleFullscr)
		self.root.bind("<Escape>", self.endFullscr)

	#clock() is a meth that continuously fetches time and updates label
		self.clock()					#call clock method
		self.fontUpdate()
		self.colUpdate()
		
		self.root.mainloop()			#call 'mainloop' from root object to listen for events

	def clock(self):
		clockData = datetime.now()	#fetch current time
		#clockData = datetime.strptime("Sun", "%a")	#fetch current time

	#Label way of updating time
		self.labelClock.configure(text = clockData)	#raw time information
		self.labelClock.configure(text = datetime.strftime(clockData, "%H:%M:%S\n%a, %b %d"))

		self.root.after(1000, self.clock)	#have self.root call itself after 1000ms

	def fontUpdate(self):
		width = self.root.winfo_width()
		widthR = self.root.winfo_reqwidth()
		height = self.root.winfo_height()
		heightR = self.root.winfo_reqheight()

		self.testMeas(self.clockFont['size'])
		if abs(width - widthR) > 20 and (height - heightR) > 5:
			print "widthDelta:",abs(width - widthR)
			print "heightDelta:",abs(height - heightR)
			if width < widthR or height < heightR:
				self.OnDec()
			elif width > widthR or height > heightR:
				self.OnInc()

		self.root.after(10, self.fontUpdate)	#have self.root call itself after 1000ms
	
	def OnInc(self, event=None):
		size = self.clockFont['size']
		self.clockFont.configure(size = size + 1)
		self.testMeas(size)

	def OnDec(self, event=None):
		size = self.clockFont['size']
		if size - 2 > 0:
			self.clockFont.configure(size = size - 1)
		else:
			print "smallest possible size!"
		self.testMeas(size)
	
	def testMeas(self, size):	#feel free to remove later; used to figure out window size
		width = self.root.winfo_width()
		widthR = self.root.winfo_reqwidth()
		height = self.root.winfo_height()
		heightR = self.root.winfo_reqheight()
		print("width:", width)
		print("widthR:", widthR)
		print("height:", height)
		print("heightR:", heightR)
		print(size)

	def toggleFullscr(self, event=None):
		self.state = not self.state
		self.root.attributes("-fullscreen", self.state)
		return "break"

	def endFullscr(self, event=None):
		self.state = False
		self.root.attributes("-fullscreen", False)
		return "break"

	def colUpdate(self, event=None):
		global bgCol
		global fgCol
		self.labelClock.configure(bg = bgCol, fg = fgCol)
		self.labelPage.configure(bg = bgCol, fg = fgCol)
		self.root.configure(background = bgCol)

timeApp = TimeApp()
