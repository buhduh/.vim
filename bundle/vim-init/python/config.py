import os

from vimwrapper import *

class Config:
  '''
  TODO, not gonna worry about vars just yet?
  variable scope precedence in increasing order:
  g(global)->t(tab)->w(window)->b(buffer)
  '''

  CONF_FILE = ".viminit"

  _config = None

  def checkPath(path):
    confFile = os.path.join(path, Config.CONF_FILE)
    wrapper = VimWrapper()
    if os.path.exists(confFile):
      wrapper.source(confFile)

  def load():
    wrapper = VimWrapper()  
    buff = wrapper.getBuffer()
    pathComponents = os.path.dirname(buff.name).strip(os.sep).split(os.sep)
    curr = "%s%s" % (os.sep, pathComponents[0])
    Config.checkPath(curr)
    for p in pathComponents[1:]:
      curr = os.path.join(curr, p)
      Config.checkPath(curr)
      
