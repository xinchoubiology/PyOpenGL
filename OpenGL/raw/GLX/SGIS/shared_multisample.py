'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_SGIS_shared_multisample'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_SGIS_shared_multisample')
GLX_MULTISAMPLE_SUB_RECT_HEIGHT_SGIS=_C('GLX_MULTISAMPLE_SUB_RECT_HEIGHT_SGIS',0x8027)
GLX_MULTISAMPLE_SUB_RECT_WIDTH_SGIS=_C('GLX_MULTISAMPLE_SUB_RECT_WIDTH_SGIS',0x8026)

