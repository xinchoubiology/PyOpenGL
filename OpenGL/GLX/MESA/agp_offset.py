'''OpenGL extension MESA.agp_offset

This module customises the behaviour of the 
OpenGL.raw.GLX.MESA.agp_offset to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extensions provides a way to convert pointers in an AGP memory
	region into byte offsets into the AGP aperture.
	Note, this extension depends on GLX_NV_vertex_array_range, for which
	no real specification exists.  See GL_NV_vertex_array_range for more
	information.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/MESA/agp_offset.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLX import _types, _glgets
from OpenGL.raw.GLX.MESA.agp_offset import *
from OpenGL.raw.GLX.MESA.agp_offset import _EXTENSION_NAME

def glInitAgpOffsetMESA():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION