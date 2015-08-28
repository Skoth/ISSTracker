from Tkinter import *
import urllib2
import json

def main():
	loc = json.load(urllib2.urlopen('http://api.open-notify.org/iss-now.json'))
	print(loc)
	m = Tk()
	w = Canvas(m, width=200, height=100)
	w.pack()
	w.create_line(0, 0, 200, 100)
	w.create_line(0, 100, 200, 0, fill='red', dash=(4,4))
	w.create_rectangle(50, 25, 150, 75, fill='blue')
	w.create_text(0,0,font='Purisa',text=loc)
	mainloop()

if __name__ == '__main__':
	main()
