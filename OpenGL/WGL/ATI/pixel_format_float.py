'''OpenGL extension ATI.pixel_format_float

This module customises the behaviour of the 
OpenGL.raw.WGL.ATI.pixel_format_float to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ATI/pixel_format_float.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.WGL import _types
from OpenGL.raw.WGL.ATI.pixel_format_float import *
from OpenGL.raw.WGL.ATI.pixel_format_float import _EXTENSION_NAME

def glInitPixelFormatFloatATI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION