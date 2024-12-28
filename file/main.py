import os
import sys
from classes.file import File

def main():
    print(File("file.txt", "Hello, World!"))

if __name__ == "__main__":
    main()