from tkinter import *
from tkinter.ttk import *
import webbrowser
# import webview
from tkinterweb import HtmlFrame  # import the HTML browser
try:
    import tkinter as tk  # python3
except ImportError:
    import Tkinter as tk  # python2

root = tk.Tk()  # create the tkinter window

webbrowser.open("http://localhost:5500/")

# webview.create_window("test", "http://localhost:5500/")
# webview.start()

# frame = HtmlFrame(root)  # create HTML browser

# frame.load_website("http://localhost:5500/")  # load a website
# # attach the HtmlFrame widget to the parent window
# frame.pack(fill="both", expand=True)
# root.mainloop()
