'''OpenGL extension HP.convolution_border_modes

This module customises the behaviour of the 
OpenGL.raw.GL.HP.convolution_border_modes to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/HP/convolution_border_modes.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.HP.convolution_border_modes import *
from OpenGL.raw.GL.HP.convolution_border_modes import _EXTENSION_NAME

def glInitConvolutionBorderModesHP():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION