'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_point_sprite'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_point_sprite')
GL_COORD_REPLACE_NV=_C('GL_COORD_REPLACE_NV',0x8862)
GL_POINT_SPRITE_NV=_C('GL_POINT_SPRITE_NV',0x8861)
GL_POINT_SPRITE_R_MODE_NV=_C('GL_POINT_SPRITE_R_MODE_NV',0x8863)
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glPointParameteriNV(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glPointParameterivNV(pname,params):pass
# Calculate length of params from pname:PointParameterNameARB
