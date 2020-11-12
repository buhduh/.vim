import vim
import re

class VimWrapper:

  class _VimSingleton:

    vimPattern = re.compile(r"^([a-z])_(\w+)$")
    def __init__(self):
      pass

    def __getattr__(self, name):
      match = VimWrapper._VimSingleton.vimPattern.search(name) 
      if match:
        return vim.eval("%s:%s" % (match.group(1), match.group(2)))
      else:
        return super().__getattr__(name)

    def __setattr__(self, name, value):
      match = VimWrapper._VimSingleton.vimPattern.search(name) 
      if match:
        vim.command("let %s:%s = '%s'" % (match.group(1), match.group(2), value))
      else:
        super().__setattr__(name, value)

    def getBuffer(self):
      print("here?")
      return vim.current.buffer
  
  _instance = None
  def __init__(self):
    if not _instance:
      _instance = VimWrapper._VimSingleton()
    
  def __setattr__(self, name, value):
    VimWrapper._instance.__setattr__(name, value)

  def __getattr__(self, name):
    return VimWrapper._instance.__getattr__(name)

  def getBuffer(self):
    print("Here?")
    #TODO For w/e reason this isn't calling into the instance
    return VimWrapper._instance.getBuffer()
