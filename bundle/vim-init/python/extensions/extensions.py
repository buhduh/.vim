import vim
import os
import extensions
import re

class ExtensionBase:

  def __init__(self, wrapper):
    self.wrapper = wrapper

  def apply(self):
    raise Exception("Extension class must implement the apply method.")

  #TODO
  def isValid(self):
    return True 

def doExtensions(bufferName, wrapper):
  bufferName = bufferName.strip()
  _, dirty =  os.path.splitext(bufferName)
  cleaned = re.sub(r'\W+', '', dirty.upper())
  ext = None
  try:
    cleaned = getattr(extensions, cleaned)
    ext = cleaned(wrapper)
  except(AttributeError):
    return
  ext.apply()
