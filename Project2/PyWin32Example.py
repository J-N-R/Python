# Simple Project that uses the PyWin32 Library to take advantage of windows specific features!
#
# Description:
#   Once ran, the program will automatically take a copy of whatever is loaded in the user's clipboard,
#   And print it back to them. Then, it takes whatever's in your clipboard, and reverses it! And to prove its not a trick, you can test it yourself.
#
#   PyWin32 comes prepackaged with Anaconda, the Anaconda python installation is recommended.

import win32clipboard  # <-- a part of pywin32


print("Welcome to my Clipboard program!")
print("Using a little magic, I am going to read what you have copied to you, and then, change your clipboard to something else!")


win32clipboard.OpenClipboard()


clipboard = str(win32clipboard.GetClipboardData())


print("\nYour clipboard is...", clipboard)


clipboard = clipboard[::-1]


win32clipboard.EmptyClipboard()


win32clipboard.SetClipboardText(clipboard)


print("\nNow its reversed! Go try it out and copy and paste somewhere!")




win32clipboard.CloseClipboard()
