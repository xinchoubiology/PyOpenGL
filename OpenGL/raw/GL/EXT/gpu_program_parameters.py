'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_gpu_program_parameters'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_gpu_program_parameters')

@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLsizei,arrays.GLfloatArray)
def glProgramEnvParameters4fvEXT(target,index,count,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLsizei,arrays.GLfloatArray)
def glProgramLocalParameters4fvEXT(target,index,count,params):pass
