"""
Don't forget vim also has the concept of filetype, eg :set filetype?
Don't think I need it for now, but remember it's present
"""
import sys
import inspect
from os.path import dirname
sys.path.append(dirname(inspect.getfile(lambda: None)))
import extensions

def main():
  extensions.doExtensions(vim.current.buffer.name)

if __name__ == "__main__":
  main()
