'''OpenGL extension ARB.texture_compression_bptc

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.texture_compression_bptc to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/texture_compression_bptc.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.texture_compression_bptc import *
from OpenGL.raw.GL.ARB.texture_compression_bptc import _EXTENSION_NAME

def glInitTextureCompressionBptcARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION