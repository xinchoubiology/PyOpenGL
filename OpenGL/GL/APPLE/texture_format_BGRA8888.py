'''OpenGL extension APPLE.texture_format_BGRA8888

This module customises the behaviour of the 
OpenGL.raw.GL.APPLE.texture_format_BGRA8888 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/APPLE/texture_format_BGRA8888.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.APPLE.texture_format_BGRA8888 import *
from OpenGL.raw.GL.APPLE.texture_format_BGRA8888 import _EXTENSION_NAME

def glInitTextureFormatBgra8888APPLE():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION