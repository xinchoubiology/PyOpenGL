'''OpenGL extension SGIS.blended_overlay

This module customises the behaviour of the 
OpenGL.raw.GLX.SGIS.blended_overlay to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIS/blended_overlay.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GLX import _types
from OpenGL.raw.GLX.SGIS.blended_overlay import *

def glInitBlendedOverlaySGIS():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION