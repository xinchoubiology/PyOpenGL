'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARM_mali_program_binary'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARM_mali_program_binary')
GL_MALI_PROGRAM_BINARY_ARM=_C('GL_MALI_PROGRAM_BINARY_ARM',0x8F61)

