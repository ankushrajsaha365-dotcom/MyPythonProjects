# File Handling System

from abc import ABC, abstractmethod


class File(ABC):

    @abstractmethod
    def open(self):
        pass


class TextFile(File):
    def open(self):
        print("Opening text file in text editor")


class ImageFile(File):
    def open(self):
        print("Opening image file in image viewer")


files = [TextFile(), ImageFile()]

for file in files:
    file.open()
