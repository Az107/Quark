import gi
import os
import sys
gi.require_version('WebKit2', '4.0')

try:
    from gi.repository import WebKit2 as WebKit
except ImportError:
    print("error")

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

win = None
web = None

win = None
web = None

def getSource(webobj, frame):
    webobj.run_javascript("pid = " + str(os.getpid())[1:])
    webobj.run_javascript("initSocket();")
    print("loaded...[OK]")

def start():
    win = Gtk.Window(title="Hello World")
    web = WebKit.WebView()
    web.load_uri("file://" + str(os.getcwd()) + "/Displays/mainDisplay.html")
    web.connect("load-changed", getSource)
    win.add(web)
    win.show_all()
    win.connect("destroy", close)
    Gtk.main()

def close(garbage):
    Gtk.main_quit()
    sys.exit(0)

def navigate(display):
        web.open("file://" + str(os.getcwd()) + "/Displays/" + display + ".html")