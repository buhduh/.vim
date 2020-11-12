"""
Don't forget vim also has the concept of filetype, eg :set filetype?
Don't think I need it for now, but remember it's present
NOTE: [I: will show definitions from included headers, maybe, investigate
NOTE: look into "preview-tag"
"""
import sys
import inspect
from os.path import dirname
sys.path.append(dirname(inspect.getfile(lambda: None)))
import extensions
from vimwrapper import *

#g:vim_init_extensions = 1

def main():
  #vim.command("let g:bar = 'yolo'")
  #vim.command("echo g:bar")
  wrapper = VimWrapper()
  extensions.doExtensions(vim.current.buffer.name, wrapper)

if __name__ == "__main__":
  main()
