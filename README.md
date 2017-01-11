# smartAlarm
Project to create an IOT-type alarm clock that displays time, weather, and other information as well as communicate with your phone.

Goals:
o	displays time, date, day
o	toggle fullscreen with <F11>
o		true fullscreen for that immersive effect
o		interface scales to fit screen size
	has a countdown function
/	integrate theme functionality
	displays weather
		displays appropriate clothes based on threshholds set
			can be an easy pref file with ability to manage multiple pref files
	displays timezone
	
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
		http://stackoverflow.com/questions/4072150/how-to-change-a-widgets-font-style-without-knowing-the-widgets-font-family-siz#4073037
		scaling is easiest to implement with monospaced fonts
	color
		http://stackoverflow.com/questions/13588908/dynamically-change-widget-background-color-in-tkinter
	disabling screen sleep
		http://www.raspberry-projects.com/pi/pi-operating-systems/raspbian/gui/disable-screen-sleep
			user "Daviz" in the comments talks about installing xscreensaver and disabling the screensaver to keep screen from sleeping
		
Accessing Weather API through python scripts)https://github.com/csparpa/pyowm:

immediate todos:
o	make displayed time prettier (no floats (stuff after the decimal))
o	look into fullscreen options
o	have time resize appropriately wrt screen size

bugs:
	scaling kinda works, has some glitchy parts it gets stuck on (toggle screen size to fix?)

