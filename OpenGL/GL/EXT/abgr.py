'''OpenGL extension EXT.abgr

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.abgr to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/abgr.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.EXT.abgr import *
from OpenGL.raw.GL.EXT.abgr import _EXTENSION_NAME

def glInitAbgrEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION
from OpenGL import images as _i

_i.COMPONENT_COUNTS[ GL_ABGR_EXT ] = 4
