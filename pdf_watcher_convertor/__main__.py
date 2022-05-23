from directory_watcher.watcher import Watcher

# Most of the magic is still happening in the watcher, as the conversion has to be performed by the Handler.

w = Watcher("C:\\Users\\Cedric\\Desktop\\RNS\\data", enable_pdf_conversion=True)
w.run()
