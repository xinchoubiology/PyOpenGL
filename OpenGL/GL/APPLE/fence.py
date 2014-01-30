'''OpenGL extension APPLE.fence

This module customises the behaviour of the 
OpenGL.raw.GL.APPLE.fence to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/APPLE/fence.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.APPLE.fence import *
from OpenGL.raw.GL.APPLE.fence import _EXTENSION_NAME

def glInitFenceAPPLE():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION