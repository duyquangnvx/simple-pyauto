import pyauto
import image_search

# Example: using pyauto to write in Notepad
hwnd = pyauto.findWindow('Notepad', None)

# To write in notepad, we need the child handle because it contain write stream
hwndChild = pyauto.getChild(hwnd)
pyauto.press(hwndChild, 'Q')

