'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_deep_texture3D'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_deep_texture3D')
GL_MAX_DEEP_3D_TEXTURE_DEPTH_NV=_C('GL_MAX_DEEP_3D_TEXTURE_DEPTH_NV',0x90D1)
GL_MAX_DEEP_3D_TEXTURE_WIDTH_HEIGHT_NV=_C('GL_MAX_DEEP_3D_TEXTURE_WIDTH_HEIGHT_NV',0x90D0)

