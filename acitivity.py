import sys
import random
import time
import random

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Office/Downloads"
to_dir = "C:/Users/Office/Desktop/sorted_files"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f'hey! {event.src_path} has been created!')
    
    def on_deleted(self, event):
        print(f"{event.src_path} has been deleted!")

    def on_moved(self, event):
        print(f'{event.src_path} has been moved to other locaton.')
    
    def on_renamed(self, event):
        print(f'the file name of {event.src_path} has been changed!')
        

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(3)
        print("Running...")
except KeyboardInterrupt:
    observer.stop()
    print("Stopped!")