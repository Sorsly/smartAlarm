# smartAlarm
Project to create an IOT-type alarm clock that displays time, weather, and other information as well as communicate with your phone.

Goals:
o	displays time, date, day
	toggle fullscreen with <F11>
		true fullscreen for that immersive effect
	displays timezone
	displays weather
		displays appropriate clothes based on threshholds set
			can be an easy pref file with ability to manage multiple pref files
	
	ties in alarm function with phone, activity monitor, etc.
		bluetooth
		potentially add in audio/light output directly to smart alarm
	always viewable/input to trigger display
		input can be phone, capacitive touch button, sound, gesture based, etc.

reference:
	general info
		tutorialspoint
	text
		http://effbot.org/tkinterbook/text.htm
			(also talks about valid index parameters)
	fullscreen
		http://stackoverflow.com/questions/7966119/display-fullscreen-mode-on-tkinter#23840010	
			chosen solu doesn't actually work, try the one afterwards (code is cleaner too)
		http://stackoverflow.com/questions/6573207/fullscreen-windows-with-tkinter?rq=1
			only max screens it vs fullscreen
	scaling
		http://stackoverflow.com/questions/18252434/scaling-tkinter-widgets/18253141

immediate todos:
o	make displayed time prettier (no floats (stuff after the decimal))
	look into fullscreen options
	have time resize appropriately wrt screen size
