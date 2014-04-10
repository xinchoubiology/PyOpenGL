'''OpenGL extension VERSION.GL_1_2

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_1_2 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/GL_1_2.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.VERSION.GL_1_2 import *
from OpenGL.raw.GL.VERSION.GL_1_2 import _EXTENSION_NAME

def glInitGl12VERSION():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION
from OpenGL.GL.ARB.imaging import *
from OpenGL.GL.VERSION.GL_1_2_images import *

GL_POINT_SIZE_GRANULARITY = GL_SMOOTH_POINT_SIZE_GRANULARITY # alias
GL_POINT_SIZE_RANGE = GL_SMOOTH_POINT_SIZE_RANGE # alias
GL_LINE_WIDTH_GRANULARITY = GL_SMOOTH_LINE_WIDTH_GRANULARITY # alias
GL_LINE_WIDTH_RANGE = GL_SMOOTH_LINE_WIDTH_RANGE # alias

glDrawRangeElements = wrapper.wrapper( glDrawRangeElements ).setPyConverter(
    'indices', arrays.AsArrayOfType( 'indices', 'type' ),
).setReturnValues(
    wrapper.returnPyArgument( 'indices' )
)


