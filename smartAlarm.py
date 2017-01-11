from Tkinter import *
from datetime import datetime
import tkFont

global bgCol 
global fgCol
bgCol = "black"
fgCol = "white"

global pageNum
global pageMax
pageNum = 0
pageMax = 2

class TimeApp():
	def __init__(self):

		#Tk() is top level object containing everything else
		self.root = Tk()				#create object 
		self.root.attributes('-zoomed', True) #maximizes window so visible
		self.clockFontL = tkFont.Font(family = "Andale Mono", size = 12)
		self.clockFontM = tkFont.Font(family = "Andale Mono", size = 6)
		self.clockFontS = tkFont.Font(family = "Andale Mono", size = 3)

	#Label() is a widget under Tk()
		self.labelPage = Label(text = "Clock", font = self.clockFontS)
		self.labelClock = Label(text = "", font = self.clockFontL)	#create object
		self.labelMS = Label(text = "", font = self.clockFontM)	#millisecond widget
		#self.labelLeft = Label(text = "left")
		#self.labelRight = Label(text = "right")

	#"organize" label wrt window using grid geometry
		self.labelPage.grid(row = 0, column = 0)
		self.labelClock.grid(row = 1, column = 0, columnspan = 4)
		self.labelMS.grid(row = 2, column = 3)
		#self.labelLeft.grid(row = 2, column = 0)	
		#self.labelRight.grid(row = 2, column = 3)

		self.root.columnconfigure(1, weight = 1)	#centers wrt grid system
		self.root.rowconfigure(1, weight = 1)		#centers wrt grid system

		self.state = False	#inits fullscreen state
	#bindings
		#bindings can call functions defined with these params (self, event=None)
		self.root.bind("=", self.OnInc)	#attempted to keybind but having error
		self.root.bind("-", self.OnDec)
		self.root.bind("<F11>", self.toggleFullscr)
		self.root.bind("<Escape>", self.endFullscr)
		self.root.bind("j", self.nextScr)
		self.root.bind("k", self.prevScr)

	#clock() is a meth that continuously fetches time and updates label
		self.clock()					#call clock method
		self.fontUpdate()
		self.colUpdate()
		
		self.root.mainloop()			#call 'mainloop' from root object to listen for events

	def clock(self):
		clockData = datetime.now()	#fetch current time
		#clockData = datetime.strptime("Sun", "%a")	#fetch current time

	#Label way of updating time
		#self.labelClock.configure(text = clockData)	#raw time information
		ms = clockData.microsecond

		if ms < 125000:
			msChar = "......."
		elif ms < 250000:
			msChar = "*......"
		elif ms < 375000:
			msChar = ".*....."
		elif ms < 500000:
			msChar = "..*...."
		elif ms < 625000:
			msChar = "...*..."
		elif ms < 750000:
			msChar = "....*.."
		elif ms < 875000:
			msChar = ".....*."
		elif ms < 999999:
			msChar = "......*"
		self.labelMS.configure(text = msChar)
		self.labelClock.configure(text = datetime.strftime(clockData, "%H:%M:%S\n%a, %b %d"))

		self.root.after(50, self.clock)	#have self.root call itself after 1000ms

	def fontUpdate(self):
		width = self.root.winfo_width()
		widthR = self.root.winfo_reqwidth()
		height = self.root.winfo_height()
		heightR = self.root.winfo_reqheight()

		sizeL = self.clockFontL['size']
		self.clockFontM.configure(size = sizeL / 2)
		self.clockFontS.configure(size = sizeL / 4)

		self.testMeas(self.clockFontL['size'])
		if abs(width - widthR) > 20 and (height - heightR) > 5:
			print "widthDelta:",abs(width - widthR)
			print "heightDelta:",abs(height - heightR)
			if width < widthR or height < heightR:
				self.OnDec()
			elif width > widthR or height > heightR:
				self.OnInc()

		self.root.after(10, self.fontUpdate)	#have self.root call itself after 1000ms
	
	def colUpdate(self, event=None):
		global bgCol
		global fgCol
		self.root.configure(background = bgCol)
		self.labelClock.configure(bg = bgCol, fg = fgCol)
		self.labelMS.configure(bg = bgCol, fg = fgCol)
		self.labelPage.configure(bg = bgCol, fg = fgCol)
	
	def OnInc(self, event=None):
		size = self.clockFontL['size']
		self.clockFontL.configure(size = size + 1)
		self.testMeas(size)

	def OnDec(self, event=None):
		size = self.clockFontL['size']
		if size - 2 > 0:
			self.clockFontL.configure(size = size - 1)
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

	def nextScr(self, event=None):
		global pageNum
		if pageNum < pageMax:
			pageNum += 1
		else:
			pageNum = 0

	def prevScr(self, event=None):
		global pageNum
		if pageNum > pageMax:
			pageNum -= 1
		else:
			pageNum = pageMax

timeApp = TimeApp()
