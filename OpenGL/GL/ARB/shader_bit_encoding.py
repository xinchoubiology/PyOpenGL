'''OpenGL extension ARB.shader_bit_encoding

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.shader_bit_encoding to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/shader_bit_encoding.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.shader_bit_encoding import *
from OpenGL.raw.GL.ARB.shader_bit_encoding import _EXTENSION_NAME

def glInitShaderBitEncodingARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION