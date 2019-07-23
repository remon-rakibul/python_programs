import webbrowser
import pyperclip
import sys

inputed_adrss = sys.argv

if len(inputed_adrss) > 1:
    address = ' '.join(inputed_adrss[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)