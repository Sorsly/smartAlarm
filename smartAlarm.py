from Tkinter import *
from datetime import datetime

class TimeApp():
	def __init__(self):

		#Tk() is top level object containing everything else
		self.root = Tk()				#create object 

	#choose Label or Text way of showing time
	#Label() is a widget under Tk()
		self.label = Label(text = "")	#create object
		self.label.pack()				#"organize" label wrt window

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
		#self.label.configure(text = clockData)	#raw time information
		self.label.configure(text = datetime.strftime(clockData, "%H:%M:%S\n%a, %b %d"))

	#Text way of updating time
		#self.text.delete(("0.0"),END)		#inserts current time at current location in text
		#self.text.insert(INSERT, clockData)		#inserts current time at INSERT index

		self.root.after(1000, self.clock)	#have self.root call itself after 1000ms

timeApp = TimeApp()
