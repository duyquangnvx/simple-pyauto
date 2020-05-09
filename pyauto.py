import win32gui
import win32ui, win32con, win32api
from ctypes import windll


# hwnd = win32gui.FindWindow(None, 'Calculator')
# return path
def captureWindow(hwnd):
    # Change the line below depending on whether you want the whole window
    # or just the client area. 
    #left, top, right, bot = win32gui.GetClientRect(hwnd)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    left = int((left)/0.8)
    top = int((top)/0.8)
    right = int((right)/0.8)
    bot = int((bot)/0.8)
    
    width = right - left
    height = bot - top

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)

    saveDC.SelectObject(saveBitMap)
    #saveDC.BitBlt((0, 0), (width, height), mfcDC, (left, top), win32con.SRCCOPY)
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)
    path = 'Image\screen_shot.png'
    saveBitMap.SaveBitmapFile(saveDC, path)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    return path
    

def click(hwnd, x, y):
    lParam = win32api.MAKELONG(x, y)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam);
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam);

def findWindow(className, title):
    return win32gui.FindWindow(className, title)
    
def press(hwnd, key):
    win32api.PostMessage(hwnd, win32con.WM_CHAR, ord(key), 0)

def getChild(hwnd):
    return win32gui.GetWindow(hwnd, win32con.GW_CHILD)
