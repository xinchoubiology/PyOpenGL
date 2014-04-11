'''OpenGL extension VERSION.GL_4_0

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_4_0 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/GL_4_0.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.VERSION.GL_4_0 import *
from OpenGL.raw.GL.VERSION.GL_4_0 import _EXTENSION_NAME

def glInitGl40VERSION():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

glGetUniformdv=wrapper.wrapper(glGetUniformdv).setOutput(#
    'params',size=_glgets._glget_size_mapping,pnameArg='location',orPassIn=True
)
glGetActiveSubroutineUniformiv=wrapper.wrapper(glGetActiveSubroutineUniformiv).setOutput(#
    'values',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
# OUTPUT MULTIPLE glGetActiveSubroutineUniformName
# OUTPUT MULTIPLE glGetActiveSubroutineUniformName
# OUTPUT MULTIPLE glGetActiveSubroutineName
# OUTPUT MULTIPLE glGetActiveSubroutineName
glGetUniformSubroutineuiv=wrapper.wrapper(glGetUniformSubroutineuiv).setOutput(#
    'params',size=(1,),orPassIn=True
)
glGetProgramStageiv=wrapper.wrapper(glGetProgramStageiv).setOutput(#
    'values',size=(1,),orPassIn=True
)
glGenTransformFeedbacks=wrapper.wrapper(glGenTransformFeedbacks).setOutput(#
    'ids',size=lambda x:(x,),pnameArg='n',orPassIn=True
)
glGetQueryIndexediv=wrapper.wrapper(glGetQueryIndexediv).setOutput(#
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
### END AUTOGENERATED SECTION
from OpenGL.GL.ARB.texture_query_lod import *
from OpenGL.GL.ARB.draw_indirect import *
from OpenGL.GL.ARB.gpu_shader5 import *
from OpenGL.GL.ARB.gpu_shader_fp64 import *
from OpenGL.GL.ARB.shader_subroutine import *
from OpenGL.GL.ARB.tessellation_shader import *
from OpenGL.GL.ARB.texture_buffer_object_rgb32 import *
from OpenGL.GL.ARB.texture_cube_map_array import *
from OpenGL.GL.ARB.texture_gather import *
from OpenGL.GL.ARB.transform_feedback2 import *
from OpenGL.GL.ARB.transform_feedback3 import *
