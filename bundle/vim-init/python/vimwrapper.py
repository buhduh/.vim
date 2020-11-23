import vim
import re
import collections

class VimWrapper:

  class _VimSingleton:

    VIM_PATTERN = re.compile(r"^([a-z])_(\w+)$")
    Buffer = collections.namedtuple("Buffer", ["name", "buffer"])
    def __init__(self):
      self.ref = VimWrapper._VimSingleton

    def __getattr__(self, name):
      match = VimWrapper._VimSingleton.VIM_PATTERN.search(name) 
      if match:
        return vim.eval("%s:%s" % (match.group(1), match.group(2)))
      else:
        return super().__getattr__(name)

    def __setattr__(self, name, value):
      match = VimWrapper._VimSingleton.VIM_PATTERN.search(name) 
      if match:
        vim.command("let %s:%s = '%s'" % (match.group(1), match.group(2), value))
      else:
        super().__setattr__(name, value)

    def source(self, fileName):
      vim.command("source %s" %(fileName)) 

    #returns a named tuple, (name, buffer)
    #consider generators here for really long files
    def getBuffer(self):
      end = vim.eval("line('$')")
      name = vim.current.buffer.name
      lines = vim.current.buffer.range(1, int(end))
      return self.ref.Buffer(name, lines)
      
  _instance = None
  def __init__(self):
    if not VimWrapper._instance:
      VimWrapper._instance = VimWrapper._VimSingleton()
    
  def __setattr__(self, name, value):
    VimWrapper._instance.__setattr__(name, value)

  def __getattr__(self, name):
    return VimWrapper._instance.__getattr__(name)

  def getBuffer(self):
    return VimWrapper._instance.getBuffer()

  def source(self, fileName):
    VimWrapper._instance.source(fileName)
