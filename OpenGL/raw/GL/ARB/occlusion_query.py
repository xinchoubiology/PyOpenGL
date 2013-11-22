'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_ARB_occlusion_query'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_occlusion_query')
GL_CURRENT_QUERY_ARB=_C('GL_CURRENT_QUERY_ARB',0x8865)
GL_QUERY_COUNTER_BITS_ARB=_C('GL_QUERY_COUNTER_BITS_ARB',0x8864)
GL_QUERY_RESULT_ARB=_C('GL_QUERY_RESULT_ARB',0x8866)
GL_QUERY_RESULT_AVAILABLE_ARB=_C('GL_QUERY_RESULT_AVAILABLE_ARB',0x8867)
GL_SAMPLES_PASSED_ARB=_C('GL_SAMPLES_PASSED_ARB',0x8914)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBeginQueryARB(target,id):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteQueriesARB(n,ids):pass
@_f
@_p.types(None,_cs.GLenum)
def glEndQueryARB(target):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenQueriesARB(n,ids):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetQueryObjectivARB(id,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glGetQueryObjectuivARB(id,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetQueryivARB(target,pname,params):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsQueryARB(id):pass
