'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'WGL_ARB_extensions_string'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_ARB_extensions_string')

@_f
@_p.types(ctypes.c_char_p,_cs.HDC)
def wglGetExtensionsStringARB(hdc):pass
