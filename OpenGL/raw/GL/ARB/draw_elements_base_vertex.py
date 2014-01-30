'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_draw_elements_base_vertex'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_draw_elements_base_vertex')

@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLint)
def glDrawElementsBaseVertex(mode,count,type,indices,basevertex):pass
# Calculate length of indices from type:DrawElementsType
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLsizei,_cs.GLint)
def glDrawElementsInstancedBaseVertex(mode,count,type,indices,instancecount,basevertex):pass
# Calculate length of indices from type:DrawElementsType
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLint)
def glDrawRangeElementsBaseVertex(mode,start,end,count,type,indices,basevertex):pass
# Calculate length of indices from type:DrawElementsType
@_f
@_p.types(None,_cs.GLenum,arrays.GLsizeiArray,_cs.GLenum,arrays.GLvoidpArray,_cs.GLsizei,arrays.GLintArray)
def glMultiDrawElementsBaseVertex(mode,count,type,indices,drawcount,basevertex):pass
