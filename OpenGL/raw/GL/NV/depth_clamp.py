'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_depth_clamp'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_depth_clamp')
GL_DEPTH_CLAMP_NV=_C('GL_DEPTH_CLAMP_NV',0x864F)

