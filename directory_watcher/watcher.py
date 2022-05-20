import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def __init__(self, extension):
        self.extension = extension

    def on_any_event(self, event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            if self.extension in event.src_path:
                print(f"Document Created: {event.src_path}")


class Watcher(object):
    def __init__(self, path_to_watch:str, recursive=True, extension=".pdf"):
        self.path_to_watch = path_to_watch
        self.observer = Observer()
        self.recursive = recursive
        self.extension = extension

    def run(self):
        event_handler = Handler(self.extension)
        self.observer.schedule(event_handler, self.path_to_watch, recursive=self.recursive)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Caught an error, stopping.")

        self.observer.join()