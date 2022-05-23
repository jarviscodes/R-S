import time
from pdf2image import convert_from_path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def __init__(self, extension, enable_conversion=False):
        self.extension = extension
        self.enable_conversion = enable_conversion

    def convert_pdf_to_jpg(self, src_path):
        pages=convert_from_path(src_path)
        for i in range(len(pages)):
            pages[i].save(f'data/page_{i}_.jpg', 'JPEG')

    def on_any_event(self, event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            if self.extension in event.src_path:
                print(f"Document Created: {event.src_path}")
                print(self.enable_conversion)
                if self.enable_conversion:
                    print(f"Converting {event.src_path} to jpg.")
                    self.convert_pdf_to_jpg(event.src_path)

class Watcher(object):
    def __init__(self, path_to_watch:str, recursive=True, extension=".pdf", enable_pdf_conversion=False):
        self.path_to_watch = path_to_watch
        self.observer = Observer()
        self.recursive = recursive
        self.extension = extension
        self.enable_conversion = enable_pdf_conversion

    def run(self):
        event_handler = Handler(self.extension, enable_conversion=self.enable_conversion)
        self.observer.schedule(event_handler, self.path_to_watch, recursive=self.recursive)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Caught an error, stopping.")

        self.observer.join()