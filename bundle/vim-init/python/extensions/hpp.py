import os

from .extensions import *
from config import *

class HPP(ExtensionBase):
  
  ROOT_DIR = "include"

  def __init__(self, wrapper):
    super().__init__(wrapper)
  
  #TODO
  def isValid(self):
    if not super().isValid():
      return False
    return True

  def apply(self):
    if not self.isValid():
      return
    self.getHeaderString()
    #vBuffer = self.wrapper.getBuffer() 
    #print("name: " + vBuffer.name)
    #for line in vBuffer.buffer:
      #if(not line):
        #print(" ")
      #print(str(i) + ": " + line)
      #else:
        #print(line)

  def transformHeaderString(self, name):
    return name.translate(str.maketrans({".": "_", os.sep: "_"})).upper()

  #Keep it simple and just parse up to the include
  def getHeaderString(self):
    buff = self.wrapper.getBuffer()
    dirName = os.path.dirname(buff.name)
    components = dirName.split(HPP.ROOT_DIR)
    cLen = len(components)
    #print("components: " + str(components))
    Config.load()
    if(cLen == 0):
      raise Exception(
        "Unexpected result while searching for root include directory when parsing buffer '%s'" 
        % (buff.name)
      ) 
    elif(cLen == 1):
      print("header string: " + self.transformHeaderString(os.path.basename(buff.name)))
    #NOTE, not really sure if it 
    elif(cLen > 1):
      print("here...")
