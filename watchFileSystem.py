'''
这是一个监控文件目录的python代码，可监控指定目录下的状态，如：文件夹和文件的创建、移动、删除等。
Date：2021-12-06
Author：郑征
Tips: 该代码可以直接套用，只需要修改： path = r"/home/reve" 中的目录即可。
'''



from watchdog.observers import Observer
from watchdog.events import *
import time

class FileEventHandler(FileSystemEventHandler):

    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        super(FileEventHandler, self).on_moved(event)
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if event.is_directory:
            print(f"{ now } 文件夹由 { event.src_path } 移动至 { event.dest_path }")
        else:
            print(f"{ now } 文件由 { event.src_path } 移动至 { event.dest_path }")

    def on_created(self, event):
        super(FileEventHandler, self).on_created(event)
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if event.is_directory:
            print(f"{ now } 文件夹 { event.src_path } 创建")
        else:
            print(f"{ now } 文件 { event.src_path } 创建")

    def on_deleted(self, event):
        super(FileEventHandler, self).on_deleted(event)
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if event.is_directory:
            print(f"{ now } 文件夹 { event.src_path } 删除")
        else:
            print(f"{ now } 文件 { event.src_path } 删除")

    def on_modified(self, event):
        super(FileEventHandler, self).on_modified(event)
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if event.is_directory:
            print(f"{ now } 文件夹 { event.src_path } 修改")
        else:
            print(f"{ now } 文件 { event.src_path } 修改")


if __name__ == "__main__":
    observer = Observer()
    path = r"/home/reve"
    event_handler = FileEventHandler()
    observer.schedule(event_handler, path, True)
    print(f"监控目录 {path}")
    observer.start()
    observer.join()
