'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_framebuffer_sRGB'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_framebuffer_sRGB')
GL_FRAMEBUFFER_SRGB=_C('GL_FRAMEBUFFER_SRGB',0x8DB9)

