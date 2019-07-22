from win32gui import *
import win32gui
import win32ui
import win32api
import win32con
import math
import subprocess
import time
from pyautogui import *

def callback(hwnd, hwnds):
	if("Dofus" in GetWindowText(hwnd)):
		hwnds.append(hwnd)
	return True

def clickGauche(hwnd,pos):
	win32api.SetCursorPos(pos)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0) 
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0) 
	return True

win32api.GetAsyncKeyState(ord('H'))

hwnds = []
demarrage = False
EnumWindows(callback, hwnds)

if not hwnds :
	demarrage = True
	subprocess.Popen ("C:\\Program Files (x86)\\Dofus2\\app\\Dofus.exe")
	time.sleep( 10 )
	EnumWindows(callback, hwnds)

hwnd=hwnds[0]
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,0,1000,826,0)
win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST,0,0,1000,826,0)
p=win32gui.GetWindowRect(hwnd)

if demarrage == True:
	fermer_msg_updater=[math.floor(p[0]+((p[2]-p[0])//2)),p[1]+455]
	clickGauche(hwnd,fermer_msg_updater)
	click_mdp=[math.floor(p[0]+((p[2]-p[0])//2)),p[1]+325]
	clickGauche(hwnd,click_mdp)


#click_fenChasse=[13,183]
#clickGauche(hwnd,click_fenChasse)
win32api.SetCursorPos([13,183])
s = screenshot()
pixel = s.getpixel((13,183))
if (pixel[0]==212) and (pixel[1]==255) and (pixel[2]==0):
	print("Chasse en cours !")
	y=240
	while ((pixel[0]!=41) and (pixel[1]!=36) and (pixel[2]!=26)) and (y<340):
		y+=1
		pixel = s.getpixel((240,y))
	if(y<340):
		click_jalon=[240,y]
		clickGauche(hwnd,click_jalon)
		time.sleep( 1 )
		clickGauche(hwnd,click_jalon)
	
	
		
	
	

while win32api.GetAsyncKeyState(ord('H')) == 0:
	time.sleep(1)

print("fini")		