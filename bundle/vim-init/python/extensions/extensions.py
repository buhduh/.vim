import vim
import os
import extensions
import re

class IExtension(object):
  def apply(self):
    raise Exception("Extension class must implement the apply method.")

def doExtensions(bufferName):
  bufferName = bufferName.strip()
  _, dirty =  os.path.splitext(bufferName)
  cleaned = re.sub(r'\W+', '', dirty.upper())
  ext = None
  try:
    cleaned = getattr(extensions, cleaned)
    ext = cleaned()
  except:
    return
  ext.apply()
