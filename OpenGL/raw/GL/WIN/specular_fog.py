'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_WIN_specular_fog'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_WIN_specular_fog')
GL_FOG_SPECULAR_TEXTURE_WIN=_C('GL_FOG_SPECULAR_TEXTURE_WIN',0x80EC)

