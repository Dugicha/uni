from graphics import *

winWidth  = 300
winHeight = 300
offset = 100

def drawQuad(x, y, width, height, win):
	for a in range(x, x + width):
		for b in range(y, y + height):
			Point(a, b).draw(win)

def main():
	win = GraphWin("circle", winWidth, winHeight)
	drawQuad(50, 50, 50, 100, win)
	drawQuad(200, 50, 50, 100, win)
	drawQuad(50, 200, 200, 30, win)

	win.getMouse()
	win.close()

main()