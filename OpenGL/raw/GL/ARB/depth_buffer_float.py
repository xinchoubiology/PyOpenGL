'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_depth_buffer_float'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_depth_buffer_float')
GL_DEPTH32F_STENCIL8=_C('GL_DEPTH32F_STENCIL8',0x8CAD)
GL_DEPTH_COMPONENT32F=_C('GL_DEPTH_COMPONENT32F',0x8CAC)
GL_FLOAT_32_UNSIGNED_INT_24_8_REV=_C('GL_FLOAT_32_UNSIGNED_INT_24_8_REV',0x8DAD)

