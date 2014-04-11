'''OpenGL extension APPLE.element_array

This module customises the behaviour of the 
OpenGL.raw.GL.APPLE.element_array to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides facilities to improve DrawElements style vertex
	indices submission performance by allowing index arrays.  Using this
	extension these arrays can be contained inside a vertex array range and
	thus pulled directly by the graphics processor, avoiding the CPU overhead
	of touching the index data.
	
	This extension is most useful when used in conjunction with the
	APPLE_vertex_array_range extension. APPLE_vertex_array_range provides an
	interface for storing vertex array data. In cases where large amounts of
	vertex data are in use, the index data used to construct primitives
	(typically as passed to the GL through DrawElements) can impose a
	significant bandwidth burden. APPLE_element_array allows the application to
	specify independent arrays of elements, which can then be cached using
	APPLE_vertex_array_range.  In effect this creates a more orthogonal
	interface for both vertex indices and data.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/APPLE/element_array.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.APPLE.element_array import *
from OpenGL.raw.GL.APPLE.element_array import _EXTENSION_NAME

def glInitElementArrayAPPLE():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION
