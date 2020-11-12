#from vimwrapper import *
from .extensions import *

class HPP(ExtensionBase):
  
  #TODO
  def isValid(self):
    if not super().isValid():
      return False
    return True

  def apply(self):
    if not self.isValid():
      return True
    vBuffer = self.wrapper.getBuffer() 
    for line in vBugger.range():
      print(line)
